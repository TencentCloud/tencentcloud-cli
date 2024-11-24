**Example 1: 更新数语信息，入参传入ip和端口**

更新数语信息，入参传入ip和端口

Input: 

```
tccli wedata UpdateDataModelRegistryInfo --cli-unfold-argument  \
    --CloudappId cloudapp-x3hadra3 \
    --AppCamRole Cloudapp_x3HADRA3_Role \
    --AppCamRoleId 4000000001321 \
    --Ip 10.2.3.4 \
    --Port 18091 \
    --VpcId vpc-96zopisr \
    --VpcRegion ap-beijing \
    --Pip 10.2.3.4 \
    --Pport 18091 \
    --IsPublic 1
```

Output: 
```
{
    "RequestId": "176da6c4-d9a5-450a-a11b-b64acd4faa60",
    "Response": {
        "Data": true,
        "RequestId": "176da6c4-d9a5-450a-a11b-b64acd4faa60"
    }
}
```

