**Example 1: 创建虚拟连接**

支持 CDC下多租户

Input: 

```
tccli vpc CreateCdcNetPlanes --cli-unfold-argument  \
    --CdcNetPlaneSet.0.VpcIds vpc-ezsladb9 \
    --CdcNetPlaneSet.0.CdcId cluster-d8htgb6k \
    --CdcNetPlaneSet.0.Name ivan \
    --CdcNetPlaneSet.0.Description ivan_Description
```

Output: 
```
{
    "Response": {
        "CdcNetPlaneSet": [
            {
                "NetPlaneId": "np-c6c48a03",
                "VpcIds": [
                    "vpc-ezsladb9"
                ],
                "CdcId": "cluster-d8htgb6k",
                "Name": "ivan",
                "Description": "ivan_Description",
                "CreateTime": "2024-01-11T16:37:50.696929",
                "UpdateTime": "2024-01-11T16:37:50.696945"
            }
        ],
        "TotalCount": 1,
        "RequestId": "f087abd5-fcca-42d0-8077-b5cae0e5f9b3"
    }
}
```

