**Example 1: 修改媒体质检模板**



Input: 

```
tccli mps ModifyQualityControlTemplate --cli-unfold-argument  \
    --Definition 200090 \
    --Name example2 \
    --Comment  \
    --QualityControlItemSet.0.Type LowEvaluation \
    --QualityControlItemSet.0.Switch OFF \
    --QualityControlItemSet.0.Threshold 60 \
    --QualityControlItemSet.0.Duration 0 \
    --QualityControlItemSet.0.IntervalTime 1000 \
    --QualityControlItemSet.1.Type Mosaic \
    --QualityControlItemSet.1.Switch OFF \
    --QualityControlItemSet.1.Duration 0 \
    --QualityControlItemSet.1.IntervalTime 0 \
    --QualityControlItemSet.2.Type CrashScreen \
    --QualityControlItemSet.2.Switch OFF \
    --QualityControlItemSet.2.Duration 0 \
    --QualityControlItemSet.2.IntervalTime 0 \
    --QualityControlItemSet.3.Type Blur \
    --QualityControlItemSet.3.Switch OFF \
    --QualityControlItemSet.3.Duration 0 \
    --QualityControlItemSet.3.IntervalTime 0 \
    --QualityControlItemSet.4.Type BlackWhiteEdge \
    --QualityControlItemSet.4.Switch OFF \
    --QualityControlItemSet.4.Duration 0 \
    --QualityControlItemSet.4.IntervalTime 0 \
    --QualityControlItemSet.5.Type LowLighting \
    --QualityControlItemSet.5.Switch OFF \
    --QualityControlItemSet.5.Duration 0 \
    --QualityControlItemSet.5.IntervalTime 0 \
    --QualityControlItemSet.6.Type HighLighting \
    --QualityControlItemSet.6.Switch OFF \
    --QualityControlItemSet.6.Duration 0 \
    --QualityControlItemSet.6.IntervalTime 0 \
    --QualityControlItemSet.7.Type NoVoice \
    --QualityControlItemSet.7.Switch OFF \
    --QualityControlItemSet.7.Duration 0 \
    --QualityControlItemSet.7.IntervalTime 0 \
    --QualityControlItemSet.8.Type LowVoice \
    --QualityControlItemSet.8.Switch OFF \
    --QualityControlItemSet.8.Duration 0 \
    --QualityControlItemSet.8.IntervalTime 0 \
    --QualityControlItemSet.9.Type HighVoice \
    --QualityControlItemSet.9.Switch OFF \
    --QualityControlItemSet.9.Duration 0 \
    --QualityControlItemSet.9.IntervalTime 0 \
    --QualityControlItemSet.10.Type VideoResolutionChanged \
    --QualityControlItemSet.10.Switch ON \
    --QualityControlItemSet.11.Type AudioSampleRateChanged \
    --QualityControlItemSet.11.Switch ON \
    --QualityControlItemSet.12.Type AudioChannelsChanged \
    --QualityControlItemSet.12.Switch ON \
    --QualityControlItemSet.13.Type ParameterSetsChanged \
    --QualityControlItemSet.13.Switch ON \
    --QualityControlItemSet.14.Type DarOrSarInvalid \
    --QualityControlItemSet.14.Switch ON \
    --QualityControlItemSet.15.Type TimestampFallback \
    --QualityControlItemSet.15.Switch ON \
    --QualityControlItemSet.16.Type DtsJitter \
    --QualityControlItemSet.16.Switch ON \
    --QualityControlItemSet.17.Type PtsJitter \
    --QualityControlItemSet.17.Switch ON \
    --QualityControlItemSet.18.Type AACDurationDeviation \
    --QualityControlItemSet.18.Switch ON \
    --QualityControlItemSet.19.Type AudioDroppingFrames \
    --QualityControlItemSet.19.Switch ON \
    --QualityControlItemSet.20.Type VideoDroppingFrames \
    --QualityControlItemSet.20.Switch ON \
    --QualityControlItemSet.21.Type AVTimestampInterleave \
    --QualityControlItemSet.21.Switch ON \
    --QualityControlItemSet.22.Type PtsLessThanDts \
    --QualityControlItemSet.22.Switch ON \
    --QualityControlItemSet.23.Type ReceiveFpsJitter \
    --QualityControlItemSet.23.Switch ON \
    --QualityControlItemSet.24.Type ReceiveFpsTooSmall \
    --QualityControlItemSet.24.Switch ON \
    --QualityControlItemSet.25.Type FpsJitter \
    --QualityControlItemSet.25.Switch ON \
    --QualityControlItemSet.26.Type StreamOpenFailed \
    --QualityControlItemSet.26.Switch ON \
    --QualityControlItemSet.27.Type StreamEnd \
    --QualityControlItemSet.27.Switch ON \
    --QualityControlItemSet.28.Type StreamParseFailed \
    --QualityControlItemSet.28.Switch ON \
    --QualityControlItemSet.29.Type VideoFirstFrameNotIdr \
    --QualityControlItemSet.29.Switch ON \
    --QualityControlItemSet.30.Type StreamNALUError \
    --QualityControlItemSet.30.Switch ON \
    --QualityControlItemSet.31.Type TsStreamNoAud \
    --QualityControlItemSet.31.Switch ON \
    --QualityControlItemSet.32.Type AudioStreamLack \
    --QualityControlItemSet.32.Switch ON \
    --QualityControlItemSet.33.Type VideoStreamLack \
    --QualityControlItemSet.33.Switch ON \
    --QualityControlItemSet.34.Type LackAudioRecover \
    --QualityControlItemSet.34.Switch ON \
    --QualityControlItemSet.35.Type LackVideoRecover \
    --QualityControlItemSet.35.Switch ON \
    --QualityControlItemSet.36.Type VideoBitrateOutofRange \
    --QualityControlItemSet.36.Switch ON \
    --QualityControlItemSet.37.Type AudioBitrateOutofRange \
    --QualityControlItemSet.37.Switch ON \
    --QualityControlItemSet.38.Type VideoDecodeFailed \
    --QualityControlItemSet.38.Switch ON \
    --QualityControlItemSet.39.Type AudioDecodeFailed \
    --QualityControlItemSet.39.Switch ON \
    --QualityControlItemSet.40.Type AudioOutOfPhase \
    --QualityControlItemSet.40.Switch ON \
    --QualityControlItemSet.41.Type VideoDuplicatedFrame \
    --QualityControlItemSet.41.Switch ON \
    --QualityControlItemSet.42.Type AudioDuplicatedFrame \
    --QualityControlItemSet.42.Switch ON \
    --QualityControlItemSet.43.Type VideoRotation \
    --QualityControlItemSet.43.Switch ON \
    --QualityControlItemSet.44.Type TsMultiPrograms \
    --QualityControlItemSet.44.Switch ON \
    --QualityControlItemSet.45.Type Mp4InvalidCodecFourcc \
    --QualityControlItemSet.45.Switch ON \
    --QualityControlItemSet.46.Type HLSBadM3u8Format \
    --QualityControlItemSet.46.Switch ON \
    --QualityControlItemSet.47.Type HLSInvalidMasterM3u8 \
    --QualityControlItemSet.47.Switch ON \
    --QualityControlItemSet.48.Type HLSInvalidMediaM3u8 \
    --QualityControlItemSet.48.Switch ON \
    --QualityControlItemSet.49.Type HLSMasterM3u8Recommended \
    --QualityControlItemSet.49.Switch ON \
    --QualityControlItemSet.50.Type HLSMediaM3u8Recommended \
    --QualityControlItemSet.50.Switch ON \
    --QualityControlItemSet.51.Type HLSMediaM3u8DiscontinuityExist \
    --QualityControlItemSet.51.Switch ON \
    --QualityControlItemSet.52.Type HLSMediaSegmentsStreamNumChange \
    --QualityControlItemSet.52.Switch ON \
    --QualityControlItemSet.53.Type HLSMediaSegmentsPTSJitterDeviation \
    --QualityControlItemSet.53.Switch ON \
    --QualityControlItemSet.54.Type HLSMediaSegmentsDTSJitterDeviation \
    --QualityControlItemSet.54.Switch ON \
    --QualityControlItemSet.55.Type TimecodeTrackExist \
    --QualityControlItemSet.55.Switch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "7c43b64a-8f21-4c2e-ab6e-a490ee5c439d"
    }
}
```

