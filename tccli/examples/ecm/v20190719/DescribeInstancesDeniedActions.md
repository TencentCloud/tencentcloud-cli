**Example 1: 获取禁止的操作列表**



Input: 

```
tccli ecm DescribeInstancesDeniedActions --cli-unfold-argument  \
    --InstanceIdSet ein-19828lyz ein-198302ok
```

Output: 
```
{
    "Response": {
        "RequestId": "78ed3f8b-e1d4-48ad-a4a3-2164e2f528c5",
        "enstanceOperatorSet": [
            {
                "enstanceId": "ein-198302ok",
                "DeniedActions": [
                    {
                        "Action": "Startenstances",
                        "Code": "InvalidenstanceState.Running",
                        "Message": "The request does not support the enstance `ein-198302ok` which is in the state of `RUNNING`."
                    },
                    {
                        "Action": "ModifyenstanceDiskType",
                        "Code": "InvalidenstanceState.Running",
                        "Message": "The request does not support the enstance `ein-198302ok` which is in the state of `RUNNING`."
                    },
                    {
                        "Action": "CopyenstanceDisk",
                        "Code": "InvalidenstanceState.Running",
                        "Message": "The request does not support the enstance `ein-198302ok` which is in the state of `RUNNING`."
                    },
                    {
                        "Action": "ModifyenstancesRenewFlag",
                        "Code": "InvalidenstanceChargeType.PostpaidByHour",
                        "Message": "The request does not support the enstance `ein-198302ok` whose charge type is `POSTPAID_BY_HOUR`."
                    },
                    {
                        "Action": "ModifyenstanceInternetChargeType",
                        "Code": "InvalidenstanceChargeType.PostpaidByHour",
                        "Message": "The request does not support the enstance `ein-198302ok` whose charge type is `POSTPAID_BY_HOUR`."
                    },
                    {
                        "Action": "ResizeenstanceDisks",
                        "Code": "InvalidDataDisk",
                        "Message": "The request does not support the enstance `ein-198302ok` who does not have data disk for processing."
                    },
                    {
                        "Action": "ResizeDisk",
                        "Code": "InvalidDataDisk.NoFoundPortable",
                        "Message": "The request does not support the enstance `ein-198302ok` who no found portable data disk."
                    },
                    {
                        "Action": "Renewenstances",
                        "Code": "InvalidenstanceChargeType.PostpaidByHour",
                        "Message": "The request does not support the enstance `ein-198302ok` whose charge type is `POSTPAID_BY_HOUR`."
                    }
                ]
            },
            {
                "enstanceId": "ein-19828lyz",
                "DeniedActions": [
                    {
                        "Action": "Startenstances",
                        "Code": "InvalidenstanceState.Running",
                        "Message": "The request does not support the enstance `ein-19828lyz` which is in the state of `RUNNING`."
                    },
                    {
                        "Action": "ModifyenstanceDiskType",
                        "Code": "InvalidenstanceState.Running",
                        "Message": "The request does not support the enstance `ein-19828lyz` which is in the state of `RUNNING`."
                    },
                    {
                        "Action": "CopyenstanceDisk",
                        "Code": "InvalidenstanceState.Running",
                        "Message": "The request does not support the enstance `ein-19828lyz` which is in the state of `RUNNING`."
                    },
                    {
                        "Action": "ModifyenstancesRenewFlag",
                        "Code": "InvalidenstanceChargeType.PostpaidByHour",
                        "Message": "The request does not support the enstance `ein-19828lyz` whose charge type is `POSTPAID_BY_HOUR`."
                    },
                    {
                        "Action": "ModifyenstanceInternetChargeType",
                        "Code": "InvalidenstanceChargeType.PostpaidByHour",
                        "Message": "The request does not support the enstance `ein-19828lyz` whose charge type is `POSTPAID_BY_HOUR`."
                    },
                    {
                        "Action": "ResizeenstanceDisks",
                        "Code": "InvalidDataDisk",
                        "Message": "The request does not support the enstance `ein-19828lyz` who does not have data disk for processing."
                    },
                    {
                        "Action": "ResizeDisk",
                        "Code": "InvalidDataDisk.NoFoundPortable",
                        "Message": "The request does not support the enstance `ein-19828lyz` who no found portable data disk."
                    },
                    {
                        "Action": "Renewenstances",
                        "Code": "InvalidenstanceChargeType.PostpaidByHour",
                        "Message": "The request does not support the enstance `ein-19828lyz` whose charge type is `POSTPAID_BY_HOUR`."
                    }
                ]
            }
        ]
    }
}
```

