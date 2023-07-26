**Example 1: 更新场景**

更新场景

Input: 

```
tccli pts UpdateScenario --cli-unfold-argument  \
    --ScenarioId scenario-abc \
    --Name pts-js(2023-05-12 16:12:30) \
    --Description  \
    --Type pts-js \
    --Load.LoadSpec.Concurrency.IterationCount 0 \
    --Load.LoadSpec.Concurrency.MaxRequestsPerSecond 0 \
    --Load.LoadSpec.Concurrency.Stages.0.DurationSeconds 120 \
    --Load.LoadSpec.Concurrency.Stages.0.TargetVirtualUsers 2 \
    --Load.LoadSpec.Concurrency.Stages.1.DurationSeconds 120 \
    --Load.LoadSpec.Concurrency.Stages.1.TargetVirtualUsers 4 \
    --Load.LoadSpec.Concurrency.Stages.2.DurationSeconds 120 \
    --Load.LoadSpec.Concurrency.Stages.2.TargetVirtualUsers 5 \
    --Load.LoadSpec.Concurrency.Stages.3.DurationSeconds 240 \
    --Load.LoadSpec.Concurrency.Stages.3.TargetVirtualUsers 5 \
    --Load.LoadSpec.Concurrency.Resources 1 \
    --Load.GeoRegionsLoadDistribution.0.Region ap-guangzhou \
    --Load.GeoRegionsLoadDistribution.0.RegionId 1 \
    --Load.GeoRegionsLoadDistribution.0.Percentage 100 \
    --Status 2 \
    --ProjectId project-abc \
    --TestScripts.0.Type js \
    --TestScripts.0.Name script.js \
    --TestScripts.0.Size 896 \
    --TestScripts.0.EncodedContent Ly8gU2VuZCBhIGh0dHAgZ2V0IHJlcXVlc3QKaW1wb3J0IGh0dHAgZnJvbSAncHRzL2h0dHAnOwppbXBvcnQgeyBjaGVjaywgc2xlZXAgfSBmcm9tICdwdHMnOwoKZXhwb3J0IGRlZmF1bHQgZnVuY3Rpb24gKCkgewogIC8vIHNpbXBsZSBnZXQgcmVxdWVzdAogIGNvbnN0IHJlc3AxID0gaHR0cC5nZXQoJ2h0dHA6Ly9tb2NraHR0cGJpbi5wdHMuc3ZjLmNsdXN0ZXIubG9jYWwvZ2V0Jyk7CiAgY29uc29sZS5sb2cocmVzcDEuYm9keSk7CiAgLy8gaWYgcmVzcDEuYm9keSBpcyBhIGpzb24gc3RyaW5nLCByZXNwMS5qc29uKCkgdHJhbnNmZXIganNvbiBmb3JtYXQgYm9keSB0byBhIGpzb24gb2JqZWN0CiAgY29uc29sZS5sb2cocmVzcDEuanNvbigpKTsKICBjaGVjaygnc3RhdHVzIGlzIDIwMCcsICgpID0+IHJlc3AxLnN0YXR1c0NvZGUgPT09IDIwMCwgcmVzcDEpOwoKICAvLyBzbGVlcCAxIHNlY29uZAogIHNsZWVwKDEpOwoKICAvLyBnZXQgcmVxdWVzdCB3aXRoIGhlYWRlcnMgYW5kIHBhcmFtZXRlcnMKICBjb25zdCByZXNwMiA9IGh0dHAuZ2V0KCdodHRwOi8vbW9ja2h0dHBiaW4ucHRzLnN2Yy5jbHVzdGVyLmxvY2FsL2dldCcsIHsKICAgIGhlYWRlcnM6IHsKICAgICAgQ29ubmVjdGlvbjogJ2tlZXAtYWxpdmUnLAogICAgICAnVXNlci1BZ2VudCc6ICdwdHMtZW5naW5lJywKICAgIH0sCiAgICBxdWVyeTogewogICAgICBuYW1lMTogJ3ZhbHVlMScsCiAgICAgIG5hbWUyOiAndmFsdWUyJywKICAgIH0sCiAgfSk7CgogIGNvbnNvbGUubG9nKHJlc3AyLmpzb24oKS5hcmdzLm5hbWUxKTsgLy8gJ3ZhbHVlMScKICBjaGVjaygnYm9keS5hcmdzLm5hbWUxIGVxdWFscyB2YWx1ZTEnLCAoKSA9PiByZXNwMi5qc29uKCkuYXJncy5uYW1lMSA9PT0gJ3ZhbHVlMScsIHJlc3AyKTsKfQo= \
    --TestScripts.0.LoadWeight 100 \
    --TestScripts.0.UpdatedAt 2023-05-12T16:12:31+08:00 \
    --TestScripts.0.EncodedHttpArchive  \
    --Owner abc
```

Output: 
```
{
    "Response": {
        "RequestId": "31446d02-c4f3-4a53-9efe-b5ad18cfcb7f"
    }
}
```

