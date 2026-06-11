**Example 1: 修改周期策略**



Input: 

```
tccli cynosdb ModifyClusterPeriodScalePolicy --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xdbsbsgg \
    --PolicyId cynosdbmysql-spd-rye0gd5b \
    --MaxCpu 4
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

