**Example 1: 创建场景**

创建场景

Input: 

```
tccli pts CreateScenario --cli-unfold-argument  \
    --Load.VpcLoadDistribution.VpcId abc \
    --Load.VpcLoadDistribution.Region ap-guangzhou \
    --Load.VpcLoadDistribution.RegionId 1 \
    --Load.GeoRegionsLoadDistribution.0.Region ap-guangzhou \
    --Load.GeoRegionsLoadDistribution.0.RegionId 1 \
    --Load.GeoRegionsLoadDistribution.0.Percentage 30 \
    --Load.GeoRegionsLoadDistribution.1.Region ap-shanghai \
    --Load.GeoRegionsLoadDistribution.1.RegionId 5 \
    --Load.GeoRegionsLoadDistribution.1.Percentage 70 \
    --Load.LoadSpec.Concurrency.MaxRequestsPerSecond 1000 \
    --Load.LoadSpec.Concurrency.Stages.0.DurationSeconds 60 \
    --Load.LoadSpec.Concurrency.Stages.0.TargetVirtualUsers 1000 \
    --Load.LoadSpec.Concurrency.IterationCount 5 \
    --Datasets.0.HeaderInFile True \
    --Datasets.0.Name data.csv \
    --Datasets.0.LineCount 300 \
    --Datasets.0.Split True \
    --Datasets.0.UpdatedAt 2020-09-22T00:00:00+00:00 \
    --Datasets.0.HeaderColumns a1 \
    --Datasets.0.Size 3000 \
    --Name scenario-a \
    --ProjectId project-a \
    --Scripts b.js \
    --Configs c.prop \
    --Type pts-js \
    --Description Description
```

Output: 
```
{
    "Response": {
        "RequestId": "31446d02-c4f3-4a53-9efe-b5ad18cfcb7f",
        "ScenarioId": "scenario-a"
    }
}
```

