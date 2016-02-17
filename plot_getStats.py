# -*- coding: utf-8 -*-
"""
Plot the parsing result from formated_getStats.json

"""
import numpy as np

import logging
import json

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation

"""
Template for refering
{
        "audio": {
            "availableBandwidth": "0.0",
            "bytesSent": "583187",
            "inputLevel": "1172",
            "packetsLost": "0",
            "packetsSent": "5836",
            "rtt": "1"
        },
        "connectionType": {
            "local": {
                "candidateType": "local",
                "ipAddress": "10.239.158.58:33178"
            },
            "remote": {
                "candidateType": "local",
                "ipAddress": "10.239.158.58:51376"
            },
            "transport": "udp"
        },
        "results": [
            {
                "googInitiator": "true",
                "id": "googLibjingleSession_1798410545927275855",
                "timestamp": "2016-02-16T08:54:30.641Z",
                "type": "googLibjingleSession"
            },
            {
                "googTrackId": "16219d27-9d29-4723-baef-98970201019b",
                "id": "googTrack_16219d27-9d29-4723-baef-98970201019b",
                "timestamp": "2016-02-16T08:54:30.641Z",
                "type": "googTrack"
            },
            {
                "googTrackId": "e25e6a43-4011-4529-97d2-cee5b72f4ecf",
                "id": "googTrack_e25e6a43-4011-4529-97d2-cee5b72f4ecf",
                "timestamp": "2016-02-16T08:54:30.641Z",
                "type": "googTrack"
            },
            {
                "googTrackId": "a0",
                "id": "googTrack_a0",
                "timestamp": "2016-02-16T08:54:30.641Z",
                "type": "googTrack"
            },
            {
                "googTrackId": "v0",
                "id": "googTrack_v0",
                "timestamp": "2016-02-16T08:54:30.641Z",
                "type": "googTrack"
            },
            {
                "googDerBase64": "MIIBmTCCAQKgAwIBAgIET+H4TzANBgkqhkiG9w0BAQsFADARMQ8wDQYDVQQDDAZXZWJSVEMwHhcNMTYwMjA0MDMxMDEwWhcNMTYwMzA1MDMxMDEwWjARMQ8wDQYDVQQDDAZXZWJSVEMwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBANvStuGRDE6Xql9LsL3QMca8ywg+rXhuuNZ2zx1ruZjJJ+uer/QyfuHb+ysCS8MFQmDSq676r+qKlZ99XY2V3Dgypj4Wfa2JL02iG4DlCpYcp33FKyVJ+TsqK4ig4GEoClK/OjKMhWQE5B/X/0LfeRJCJ2H4sC15RfYRr5FuVB0PAgMBAAEwDQYJKoZIhvcNAQELBQADgYEAZOkq/aQ8RJSpS9NBo9iFsYwqZfr6zdkbSnMK6ej0eg/uj7ZVRVQZo0jJX5DOacE4ALJN+HNJw4JbvjwM9rwbEctm4lXB+Ps86SEV1SjptK2j4CqSoHFt5EcOgbIou3p5AYWNs2hQv5pQYBxvWnP4dwoG6e11E7wz0b0TyYHOVM4=",
                "googFingerprint": "25:07:A0:FB:D9:69:8B:6A:6F:CE:E0:B0:74:3D:B8:05:D3:0D:62:82:D5:F8:13:0F:97:65:02:50:CC:65:9A:8C",
                "googFingerprintAlgorithm": "sha-256",
                "id": "googCertificate_25:07:A0:FB:D9:69:8B:6A:6F:CE:E0:B0:74:3D:B8:05:D3:0D:62:82:D5:F8:13:0F:97:65:02:50:CC:65:9A:8C",
                "timestamp": "2016-02-16T08:53:33.116Z",
                "type": "googCertificate"
            },
            {
                "googDerBase64": "MIIDsTCCApmgAwIBAgIJANpjnWPWCZHdMA0GCSqGSIb3DQEBCwUAMG8xCzAJBgNVBAYTAkNOMREwDwYDVQQIDAhTaGFuZ2hhaTERMA8GA1UEBwwIU2hhbmdoYWkxDjAMBgNVBAoMBUludGVsMQ8wDQYDVQQLDAZXZWJSVEMxGTAXBgNVBAMMEHdlYnJ0Yy5pbnRlbC5jb20wHhcNMTUwOTI5MDM0MzAzWhcNMTUxMjMxMDM0MzAzWjBvMQswCQYDVQQGEwJDTjERMA8GA1UECAwIU2hhbmdoYWkxETAPBgNVBAcMCFNoYW5naGFpMQ4wDAYDVQQKDAVJbnRlbDEPMA0GA1UECwwGV2ViUlRDMRkwFwYDVQQDDBB3ZWJydGMuaW50ZWwuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArMHIZeXhtXZVrj283fIRX5QvxCHkpYPhhckiUZRCAgWTp5JZIW3GjrqqY0aJBrPApuw/Pt7HSm4Cm9Cu80PLoZQppuA6hM3n30PUNWfCqckcKL4rXaXlUhag0Xfgs0zazsVdSIFGaiqltb87c/ewHVwCd7Vi25K9snq5e7MUqfxCfEEubzGMJN0EqhbbvGVdDaOMbcWkiFJaBkJQTKphve9zxxOarmCHkjiaBY4WQ0lmecCYP4mk5dSm6ROK5otU6xmvBUB6Bct64kwXk8UCa/uzLgbfRWqxSBpBzpmW/NdcAOT6QXjwU5t9DpAI2ye0gZilQmzzGsC/K7ECcTDpcwIDAQABo1AwTjAdBgNVHQ4EFgQUkbSiF4Dh4TsALrDrO+3y83ubeTEwHwYDVR0jBBgwFoAUkbSiF4Dh4TsALrDrO+3y83ubeTEwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAUPPtkNf1Zun4DuuxkGlifbg5ftlMgNU7GNe8OT1dE2DGp/y0fNr1k+t1gE+d29SsTx9USoVxX/DWvuOUhyn7JSNW21IvaAmOlzaM9LLjbQvyzStGf5HbJkMLYFD5fF01Y25aUh0NL+MJ3sdAjVBox/V7gruK3GPSNSormCYexVGhWnB4/1EPe2tEZ0kD9RlRmVuKsZcObF4rCqg1/uDklLppblrefjCEQhmbNOebDX0BTIxFy28gCIYYbVHfNa8zRURw4urjp/m+rKlUDtiU2nhnM4+BcNu509IKrT2+YD32t2r2HlPHeFfn+IHOZ8vY1EUBd5jGaTjcIljVbiKy7g==",
                "googFingerprint": "B4:A3:C3:C0:19:49:44:67:F7:BF:F7:AE:E1:DF:E6:E5:A7:91:06:6E:B5:05:A8:59:C6:EE:D5:7F:F6:05:CC:90",
                "googFingerprintAlgorithm": "sha-256",
                "id": "googCertificate_B4:A3:C3:C0:19:49:44:67:F7:BF:F7:AE:E1:DF:E6:E5:A7:91:06:6E:B5:05:A8:59:C6:EE:D5:7F:F6:05:CC:90",
                "timestamp": "2016-02-16T08:53:33.116Z",
                "type": "googCertificate"
            },
            {
                "dtlsCipher": "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
                "googComponent": "1",
                "id": "Channel-audio-1",
                "localCertificateId": "googCertificate_25:07:A0:FB:D9:69:8B:6A:6F:CE:E0:B0:74:3D:B8:05:D3:0D:62:82:D5:F8:13:0F:97:65:02:50:CC:65:9A:8C",
                "remoteCertificateId": "googCertificate_B4:A3:C3:C0:19:49:44:67:F7:BF:F7:AE:E1:DF:E6:E5:A7:91:06:6E:B5:05:A8:59:C6:EE:D5:7F:F6:05:CC:90",
                "selectedCandidatePairId": "Conn-audio-1-0",
                "srtpCipher": "AES_CM_128_HMAC_SHA1_80",
                "timestamp": "2016-02-16T08:53:33.116Z",
                "type": "googComponent"
            },
            {
                "bytesReceived": "17705",
                "bytesSent": "5150196",
                "googActiveConnection": "true",
                "googChannelId": "Channel-audio-1",
                "googLocalAddress": "10.239.158.58:33178",
                "googLocalCandidateType": "local",
                "googReadable": "true",
                "googRemoteAddress": "10.239.158.58:51376",
                "googRemoteCandidateType": "local",
                "googRtt": "0",
                "googTransportType": "udp",
                "googWritable": "true",
                "id": "Conn-audio-1-0",
                "localCandidateId": "Cand-yyG+54I5",
                "packetsDiscardedOnSend": "0",
                "packetsSent": "10838",
                "remoteCandidateId": "Cand-V8O7DxH+",
                "timestamp": "2016-02-16T08:53:33.116Z",
                "type": "googCandidatePair"
            },
            {
                "candidateType": "host",
                "id": "Cand-yyG+54I5",
                "ipAddress": "10.239.158.58",
                "networkType": "lan",
                "portNumber": "33178",
                "priority": "2122260223",
                "timestamp": "2016-02-16T08:51:36.541Z",
                "transport": "udp",
                "type": "localcandidate"
            },
            {
                "candidateType": "host",
                "id": "Cand-V8O7DxH+",
                "ipAddress": "10.239.158.58",
                "portNumber": "51376",
                "priority": "2013266431",
                "timestamp": "2016-02-16T08:51:36.541Z",
                "transport": "udp",
                "type": "remotecandidate"
            },
            {
                "audioOutputLevel": "-1",
                "bytesReceived": "0",
                "googAccelerateRate": "0",
                "googCaptureStartNtpTimeMs": "0",
                "googCodecName": "",
                "googCurrentDelayMs": "0",
                "googDecodingCNG": "0",
                "googDecodingCTN": "0",
                "googDecodingCTSG": "0",
                "googDecodingNormal": "0",
                "googDecodingPLC": "0",
                "googDecodingPLCCNG": "0",
                "googExpandRate": "0",
                "googJitterBufferMs": "0",
                "googJitterReceived": "0",
                "googPreemptiveExpandRate": "0",
                "googPreferredJitterBufferMs": "0",
                "googSecondaryDecodedRate": "0",
                "googSpeechExpandRate": "0",
                "googTrackId": "a0",
                "id": "ssrc_44444_recv",
                "packetsLost": "0",
                "packetsReceived": "0",
                "ssrc": "44444",
                "timestamp": "2016-02-16T08:53:33.116Z",
                "transportId": "Channel-audio-1",
                "type": "ssrc"
            },
            {
                "audioInputLevel": "1172",
                "bytesSent": "583187",
                "googCodecName": "opus",
                "googEchoCancellationEchoDelayMedian": "-1",
                "googEchoCancellationEchoDelayStdDev": "-1",
                "googEchoCancellationQualityMin": "-1",
                "googEchoCancellationReturnLoss": "-100",
                "googEchoCancellationReturnLossEnhancement": "-100",
                "googJitterReceived": "19",
                "googRtt": "1",
                "googTrackId": "16219d27-9d29-4723-baef-98970201019b",
                "googTypingNoiseState": "false",
                "id": "ssrc_649077998_send",
                "packetsLost": "0",
                "packetsSent": "5836",
                "ssrc": "649077998",
                "timestamp": "2016-02-16T08:53:33.116Z",
                "transportId": "Channel-audio-1",
                "type": "ssrc"
            },
            {
                "bytesReceived": "0",
                "googCaptureStartNtpTimeMs": "0",
                "googCodecName": "",
                "googCurrentDelayMs": "0",
                "googDecodeMs": "0",
                "googFirsSent": "0",
                "googFrameHeightReceived": "-1",
                "googFrameRateDecoded": "0",
                "googFrameRateOutput": "0",
                "googFrameRateReceived": "0",
                "googFrameWidthReceived": "-1",
                "googJitterBufferMs": "0",
                "googMaxDecodeMs": "0",
                "googMinPlayoutDelayMs": "0",
                "googNacksSent": "0",
                "googPlisSent": "0",
                "googRenderDelayMs": "10",
                "googTargetDelayMs": "10",
                "googTrackId": "v0",
                "id": "ssrc_55543_recv",
                "packetsLost": "0",
                "packetsReceived": "0",
                "ssrc": "55543",
                "timestamp": "2016-02-16T08:53:33.116Z",
                "transportId": "Channel-audio-1",
                "type": "ssrc"
            },
            {
                "bytesSent": "4446633",
                "googAdaptationChanges": "0",
                "googAvgEncodeMs": "6",
                "googBandwidthLimitedResolution": "false",
                "googCodecName": "VP8",
                "googCpuLimitedResolution": "false",
                "googEncodeUsagePercent": "15",
                "googFirsReceived": "0",
                "googFrameHeightInput": "480",
                "googFrameHeightSent": "480",
                "googFrameRateInput": "16",
                "googFrameRateSent": "16",
                "googFrameWidthInput": "640",
                "googFrameWidthSent": "640",
                "googNacksReceived": "0",
                "googPlisReceived": "0",
                "googRtt": "2",
                "googTrackId": "e25e6a43-4011-4529-97d2-cee5b72f4ecf",
                "googViewLimitedResolution": "false",
                "id": "ssrc_3725716268_send",
                "packetsLost": "0",
                "packetsSent": "4720",
                "ssrc": "3725716268",
                "timestamp": "2016-02-16T08:53:33.116Z",
                "transportId": "Channel-audio-1",
                "type": "ssrc"
            },
            {
                "googActualEncBitrate": "292396",
                "googAvailableReceiveBandwidth": "0",
                "googAvailableSendBandwidth": "300000",
                "googBucketDelay": "0",
                "googRetransmitBitrate": "0",
                "googTargetEncBitrate": "300000",
                "googTransmitBitrate": "295795",
                "id": "bweforvideo",
                "timestamp": "2016-02-16T08:53:33.116Z",
                "type": "VideoBwe"
            }
        ],
        "video": {
            "availableBandwidth": "0.0",
            "bandwidth": {
                "googActualEncBitrate": "292396",
                "googAvailableReceiveBandwidth": "0",
                "googAvailableSendBandwidth": "300000",
                "googBucketDelay": "0",
                "googRetransmitBitrate": "0",
                "googTargetEncBitrate": "300000",
                "googTransmitBitrate": "295795"
            },
            "bytesSent": "4446633",
            "googAvgEncodeMs": "6",
            "googBandwidthLimitedResolution": "false",
            "googCpuLimitedResolution": "false",
            "googEncodeUsagePercent": "15",
            "googFirsReceived": "0",
            "googFrameHeightInput": "480",
            "googFrameHeightSent": "480",
            "googFrameRateInput": "16",
            "googFrameRateSent": "16",
            "googFrameWidthInput": "640",
            "googFrameWidthSent": "640",
            "googNacksReceived": "0",
            "googPlisReceived": "0",
            "googViewLimitedResolution": "false",
            "packetsLost": "0",
            "packetsSent": "4720",
            "rtt": "2"
        }
    },

"""


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def parsing_stats_json(stats_json_file):
    with open(stats_json_file, 'r') as f:
        data = json.load(f)
        
    logging.debug(data[3])
    logging.debug(json.dumps(data[3]))
#    logging.debug(data[3]['video']['packetsLost'])
#    logging.debug(data);

    f.closed
    
    return data
    



if __name__ == "__main__":
    parsing_stats_json("format_getStats.json")