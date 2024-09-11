**Example 1: 灾备回切**

无

Input: 

```
tccli cdb SwitchDrMasterRole --cli-unfold-argument  \
    --SrcInfo.InstanceId cdb-uns231ns \
    --SrcInfo.IsOverrideRoot 0 \
    --SrcInfo.RegionId 1 \
    --SrcInfo.ZoneId 100004 \
    --DstInfo.InstanceId cdb-5nv232n1 \
    --DstInfo.RegionId 1 \
    --DstInfo.ZoneId 100002
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "85b295bb-8f43-ce01-e35f-5a02e2beeeac",
        "RequestId": "95b295bb-8f43-c101-e35f-5a02e2baeaad"
    }
}
```

