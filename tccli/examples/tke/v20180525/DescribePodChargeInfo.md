**Example 1: 不输入必要参数**

 需要同时输入 Namespace 和 Name，或者 Uid

Input: 

```
tccli tke DescribePodChargeInfo --cli-unfold-argument  \
    --ClusterId cls-s180xq54
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError.Param",
            "Message": "Namespace,Name,Uid is empty"
        },
        "RequestId": "99a94acb-7566-410b-8dc8-b611ca160820"
    }
}
```

**Example 2: 只指定 Namespace**

 需要同时指定 Namespace 和 Name

Input: 

```
tccli tke DescribePodChargeInfo --cli-unfold-argument  \
    --ClusterId cls-s180xq54 \
    --Namespace default
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError.Param",
            "Message": "Namespace and Name must be set"
        },
        "RequestId": "e9de622d-82fc-4aa1-a32c-f2679bc51a9e"
    }
}
```

**Example 3: 查询多个运行中的Pod计费信息**

输入多个Uid来查询

Input: 

```
tccli tke DescribePodChargeInfo --cli-unfold-argument  \
    --ClusterId cls-0x51a7qw \
    --Uids 6c4022b4-288c-449e-b50f-ae06d91dd48e a49edc4a-b316-45b0-8ce4-8f23f93a27c7
```

Output: 
```
{
    "Response": {
        "ChargeInfoSet": [
            {
                "ChargeType": "POSTPAID_BY_HOUR",
                "Cpu": 2,
                "Memory": 4,
                "Name": "csi-cbs-controller-6678658c57-hhbvw",
                "Namespace": "kube-system",
                "StartTime": "2024-04-17 00:08:15",
                "Type": "intel",
                "Uid": "6c4022b4-288c-449e-b50f-ae06d91dd48e"
            },
            {
                "ChargeType": "NO_CHARGE",
                "Cpu": 0.25,
                "Memory": 0.5,
                "Name": "coredns-56555dd999-ntc6g",
                "Namespace": "kube-system",
                "StartTime": "2024-04-17 00:08:11",
                "Type": "intel",
                "Uid": "a49edc4a-b316-45b0-8ce4-8f23f93a27c7"
            }
        ],
        "RequestId": "9fe5a6b6-ad87-426d-b619-b600d0a18f23"
    }
}
```

**Example 4: 通过 Namespace 和 Name 查询**

同时指定了 Namespace 和 Name

Input: 

```
tccli tke DescribePodChargeInfo --cli-unfold-argument  \
    --ClusterId cls-s180xq54 \
    --Namespace default \
    --Name nginx-c4cd9685f-m58ts
```

Output: 
```
{
    "Response": {
        "ChargeInfoSet": [
            {
                "ChargeType": "POSTPAID_BY_HOUR",
                "Cpu": 1,
                "Memory": 1,
                "Name": "nginx-c4cd9685f-m58ts",
                "Namespace": "default",
                "StartTime": "2024-03-26 00:10:38",
                "Type": "intel",
                "Uid": "4df5eb56-df50-4bd4-b84e-8c3f7fdf7ab8"
            }
        ],
        "RequestId": "9b400838-e679-486f-a7d3-854d5040a6e6"
    }
}
```

