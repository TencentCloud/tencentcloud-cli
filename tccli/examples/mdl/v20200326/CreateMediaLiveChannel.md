**Example 1: Sample request**



Input: 

```
tccli mdl CreateMediaLiveChannel --cli-unfold-argument  \
    --Name channel \
    --AttachedInputs.0.Id EEEEE \
    --AttachedInputs.0.AudioSelectors.0.Name eng \
    --AttachedInputs.0.AudioSelectors.0.AudioPidSelection.Pid 256 \
    --AudioTemplates.0.Name test1 \
    --AudioTemplates.0.Acodec AAC \
    --AudioTemplates.0.AudioBitrate 112000 \
    --AudioTemplates.0.AudioSelectorName eng \
    --AudioTemplates.0.LanguageCode eng \
    --VideoTemplates.0.Name test2 \
    --VideoTemplates.0.Vcodec H264 \
    --VideoTemplates.0.VideoBitrate 1000000 \
    --VideoTemplates.0.Width 1920 \
    --VideoTemplates.0.Height 1080 \
    --VideoTemplates.0.Gop 2 \
    --VideoTemplates.0.Fps 60 \
    --OutputGroups.0.Name outputGroup \
    --OutputGroups.0.RemuxProtocol DASH \
    --OutputGroups.0.HlsRemuxSettings.SegmentDuration 2000 \
    --OutputGroups.0.HlsRemuxSettings.SegmentNumber 3 \
    --OutputGroups.0.HlsRemuxSettings.PdtInsertion OPEN \
    --OutputGroups.0.HlsRemuxSettings.PdtDuration 600 \
    --OutputGroups.0.DashRemuxSettings.SegmentDuration 2000 \
    --OutputGroups.0.DashRemuxSettings.SegmentNumber 3 \
    --OutputGroups.0.DashRemuxSettings.PeriodTriggers OPEN \
    --OutputGroups.0.DrmSettings.State OPEN \
    --OutputGroups.0.DrmSettings.ContentId 12312dsde2 \
    --OutputGroups.0.Outputs.0.Name output \
    --OutputGroups.0.Outputs.0.Scte35Settings.Behavior PASSTHROUGH \
    --OutputGroups.0.Destinations.0.OutputUrl http://domain/live/1233 \
    --OutputGroups.0.Destinations.0.AuthKey aaaa \
    --OutputGroups.0.Destinations.0.Username bbbb \
    --OutputGroups.0.Destinations.0.Password cccc
```

Output: 
```
{
    "Response": {
        "Id": "sda",
        "RequestId": "11-222-222"
    }
}
```

