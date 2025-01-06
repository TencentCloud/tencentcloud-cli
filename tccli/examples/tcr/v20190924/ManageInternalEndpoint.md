**Example 1: 管理内网接入**



Input: 

```
tccli tcr ManageInternalEndpoint --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --Operation Create \
    --VpcId vpc-74ffq7ov \
    --SubnetId subnet-kpmi5ji6
```

Output: 
```
{
    "Response": {
        "RegistryId": "tcr-dg284imq",
        "RequestId": "e842f4a4-dc50-44dc-b299-ba9b78b49584"
    }
}
```

