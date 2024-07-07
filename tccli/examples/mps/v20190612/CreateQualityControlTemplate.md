**Example 1: 创建媒体质检模板**



Input: 

```
tccli mps CreateQualityControlTemplate --cli-unfold-argument  \
    --Name example \
    --Comment  \
    --QualityControlItemSet.0.Type LowEvaluation \
    --QualityControlItemSet.0.Switch ON \
    --QualityControlItemSet.1.Type Mosaic \
    --QualityControlItemSet.1.Switch OFF \
    --QualityControlItemSet.2.Type CrashScreen \
    --QualityControlItemSet.2.Switch OFF \
    --QualityControlItemSet.3.Type Blur \
    --QualityControlItemSet.3.Switch OFF \
    --QualityControlItemSet.4.Type BlackWhiteEdge \
    --QualityControlItemSet.4.Switch OFF \
    --QualityControlItemSet.5.Type LowLighting \
    --QualityControlItemSet.5.Switch OFF \
    --QualityControlItemSet.6.Type HighLighting \
    --QualityControlItemSet.6.Switch OFF \
    --QualityControlItemSet.7.Type NoVoice \
    --QualityControlItemSet.7.Switch OFF \
    --QualityControlItemSet.8.Type LowVoice \
    --QualityControlItemSet.8.Switch OFF \
    --QualityControlItemSet.9.Type HighVoice \
    --QualityControlItemSet.9.Switch OFF \
    --QualityControlItemSet.10.Type VideoResolutionChanged \
    --QualityControlItemSet.10.Switch OFF \
    --QualityControlItemSet.11.Type AudioSampleRateChanged \
    --QualityControlItemSet.11.Switch OFF \
    --QualityControlItemSet.12.Type AudioChannelsChanged \
    --QualityControlItemSet.12.Switch OFF \
    --QualityControlItemSet.13.Type ParameterSetsChanged \
    --QualityControlItemSet.13.Switch OFF \
    --QualityControlItemSet.14.Type DarOrSarInvalid \
    --QualityControlItemSet.14.Switch OFF \
    --QualityControlItemSet.15.Type TimestampFallback \
    --QualityControlItemSet.15.Switch OFF \
    --QualityControlItemSet.16.Type DtsJitter \
    --QualityControlItemSet.16.Switch OFF \
    --QualityControlItemSet.17.Type PtsJitter \
    --QualityControlItemSet.17.Switch OFF \
    --QualityControlItemSet.18.Type AACDurationDeviation \
    --QualityControlItemSet.18.Switch OFF \
    --QualityControlItemSet.19.Type AudioDroppingFrames \
    --QualityControlItemSet.19.Switch OFF \
    --QualityControlItemSet.20.Type VideoDroppingFrames \
    --QualityControlItemSet.20.Switch OFF \
    --QualityControlItemSet.21.Type AVTimestampInterleave \
    --QualityControlItemSet.21.Switch OFF \
    --QualityControlItemSet.22.Type PtsLessThanDts \
    --QualityControlItemSet.22.Switch OFF \
    --QualityControlItemSet.23.Type ReceiveFpsJitter \
    --QualityControlItemSet.23.Switch OFF \
    --QualityControlItemSet.24.Type ReceiveFpsTooSmall \
    --QualityControlItemSet.24.Switch OFF \
    --QualityControlItemSet.25.Type FpsJitter \
    --QualityControlItemSet.25.Switch OFF \
    --QualityControlItemSet.26.Type StreamOpenFailed \
    --QualityControlItemSet.26.Switch OFF \
    --QualityControlItemSet.27.Type StreamEnd \
    --QualityControlItemSet.27.Switch OFF \
    --QualityControlItemSet.28.Type StreamParseFailed \
    --QualityControlItemSet.28.Switch OFF \
    --QualityControlItemSet.29.Type VideoFirstFrameNotIdr \
    --QualityControlItemSet.29.Switch OFF \
    --QualityControlItemSet.30.Type StreamNALUError \
    --QualityControlItemSet.30.Switch OFF \
    --QualityControlItemSet.31.Type TsStreamNoAud \
    --QualityControlItemSet.31.Switch OFF \
    --QualityControlItemSet.32.Type AudioStreamLack \
    --QualityControlItemSet.32.Switch OFF \
    --QualityControlItemSet.33.Type VideoStreamLack \
    --QualityControlItemSet.33.Switch OFF \
    --QualityControlItemSet.34.Type LackAudioRecover \
    --QualityControlItemSet.34.Switch OFF \
    --QualityControlItemSet.35.Type LackVideoRecover \
    --QualityControlItemSet.35.Switch OFF \
    --QualityControlItemSet.36.Type VideoBitrateOutofRange \
    --QualityControlItemSet.36.Switch OFF \
    --QualityControlItemSet.37.Type AudioBitrateOutofRange \
    --QualityControlItemSet.37.Switch OFF \
    --QualityControlItemSet.38.Type VideoDecodeFailed \
    --QualityControlItemSet.38.Switch OFF \
    --QualityControlItemSet.39.Type AudioDecodeFailed \
    --QualityControlItemSet.39.Switch OFF \
    --QualityControlItemSet.40.Type AudioOutOfPhase \
    --QualityControlItemSet.40.Switch OFF \
    --QualityControlItemSet.41.Type VideoDuplicatedFrame \
    --QualityControlItemSet.41.Switch OFF \
    --QualityControlItemSet.42.Type AudioDuplicatedFrame \
    --QualityControlItemSet.42.Switch OFF \
    --QualityControlItemSet.43.Type VideoRotation \
    --QualityControlItemSet.43.Switch OFF \
    --QualityControlItemSet.44.Type TsMultiPrograms \
    --QualityControlItemSet.44.Switch OFF \
    --QualityControlItemSet.45.Type Mp4InvalidCodecFourcc \
    --QualityControlItemSet.45.Switch OFF \
    --QualityControlItemSet.46.Type HLSBadM3u8Format \
    --QualityControlItemSet.46.Switch OFF \
    --QualityControlItemSet.47.Type HLSInvalidMasterM3u8 \
    --QualityControlItemSet.47.Switch OFF \
    --QualityControlItemSet.48.Type HLSInvalidMediaM3u8 \
    --QualityControlItemSet.48.Switch OFF \
    --QualityControlItemSet.49.Type HLSMasterM3u8Recommended \
    --QualityControlItemSet.49.Switch OFF \
    --QualityControlItemSet.50.Type HLSMediaM3u8Recommended \
    --QualityControlItemSet.50.Switch OFF \
    --QualityControlItemSet.51.Type HLSMediaM3u8DiscontinuityExist \
    --QualityControlItemSet.51.Switch OFF \
    --QualityControlItemSet.52.Type HLSMediaSegmentsStreamNumChange \
    --QualityControlItemSet.52.Switch OFF \
    --QualityControlItemSet.53.Type HLSMediaSegmentsPTSJitterDeviation \
    --QualityControlItemSet.53.Switch OFF \
    --QualityControlItemSet.54.Type HLSMediaSegmentsDTSJitterDeviation \
    --QualityControlItemSet.54.Switch OFF \
    --QualityControlItemSet.55.Type TimecodeTrackExist \
    --QualityControlItemSet.55.Switch OFF
```

Output: 
```
{
    "Response": {
        "Definition": 200090,
        "RequestId": "7bb44c6c-92d0-4dad-99cf-88f569c6d3ad"
    }
}
```

