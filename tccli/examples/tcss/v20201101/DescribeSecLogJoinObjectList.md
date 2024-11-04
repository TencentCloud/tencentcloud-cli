**Example 1: 查询安全日志接入对象列表**

查询安全日志接入对象列表

Input: 

```
tccli tcss DescribeSecLogJoinObjectList --cli-unfold-argument  \
    --LogType container_bash \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name Status \
    --Filters.0.Values ONLINE OFFLINE UNINSTALL \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "AutoJoin": false,
        "ExcludedCount": 0,
        "List": [
            {
                "ClusterID": "cls-q0bc0ed2",
                "ClusterMainAddress": "",
                "ClusterName": "tke2",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "v1.26.1-tke.5",
                "ContainerCnt": 23,
                "HostID": "3b6b1bbc-1c7a-47e2-9ca8-e9c27ec9d068",
                "HostIP": "172.17.1.6",
                "HostName": "tke_cls-q0bc0ed2_worker",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "159.75.90.217"
            },
            {
                "ClusterID": "cls-cuszrpiu",
                "ClusterMainAddress": "",
                "ClusterName": "测试用常驻集群_ivon",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "v1.28.3-tke.4",
                "ContainerCnt": 27,
                "HostID": "f4a8f409-0048-4c91-a58f-165750b2dc00",
                "HostIP": "10.0.3.211",
                "HostName": "tke_cls-cuszrpiu_worker",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "106.52.4.208"
            },
            {
                "ClusterID": "cls-5licssbi",
                "ClusterMainAddress": "",
                "ClusterName": "piper-容器告警接入安全中心测试",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "v1.22.5-tke.25",
                "ContainerCnt": 40,
                "HostID": "470854d7-40ff-4a3a-a2f8-b44bf99511e5",
                "HostIP": "172.17.1.53",
                "HostName": "as-tke-np-7lmwo8pi",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "42.194.189.232"
            },
            {
                "ClusterID": "cls-7dget88s",
                "ClusterMainAddress": "",
                "ClusterName": "飞舟测试-tmp",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "v1.28.3-tke.4",
                "ContainerCnt": 17,
                "HostID": "4d43d069-e9cf-49ce-9417-2cc542f6c7be",
                "HostIP": "172.17.1.56",
                "HostName": "飞舟集群测试-tmp1",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "175.178.25.145"
            },
            {
                "ClusterID": "",
                "ClusterMainAddress": "",
                "ClusterName": "",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "",
                "ContainerCnt": 0,
                "HostID": "6a874de8-c3ba-460e-99c6-5e14a6573bfc",
                "HostIP": "10.206.16.6",
                "HostName": "tcs-dev-proxy",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "118.195.143.65"
            },
            {
                "ClusterID": "",
                "ClusterMainAddress": "",
                "ClusterName": "",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "",
                "ContainerCnt": 0,
                "HostID": "192ba964-f190-4aff-8d6c-9c00251f11c3",
                "HostIP": "10.0.12.22",
                "HostName": "系统兼容性测试-ivon",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "43.136.100.158"
            },
            {
                "ClusterID": "",
                "ClusterMainAddress": "",
                "ClusterName": "",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "",
                "ContainerCnt": 5,
                "HostID": "d2f4a77b-d9c9-4161-999f-fbda13ed17fc",
                "HostIP": "172.17.1.71",
                "HostName": "v_ixnli告警测试",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "119.29.10.130"
            },
            {
                "ClusterID": "cls-7dget88s",
                "ClusterMainAddress": "",
                "ClusterName": "飞舟测试-tmp",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "v1.28.3-tke.4",
                "ContainerCnt": 17,
                "HostID": "428fb819-bc1e-4b0a-8bc1-a9fc2d6ac950",
                "HostIP": "172.17.1.11",
                "HostName": "飞舟集群测试-tmp2",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "119.91.62.58"
            },
            {
                "ClusterID": "",
                "ClusterMainAddress": "",
                "ClusterName": "",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "",
                "ContainerCnt": 1,
                "HostID": "8ff28261-b2c7-4f68-9314-453a52aa1ea0",
                "HostIP": "172.16.50.116",
                "HostName": "云镜漏洞测试机-攻击机器",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "175.178.69.167"
            },
            {
                "ClusterID": "",
                "ClusterMainAddress": "",
                "ClusterName": "",
                "ClusterStatus": "",
                "ClusterType": "",
                "ClusterVersion": "",
                "ContainerCnt": 12,
                "HostID": "380add75-bb06-4cc4-84c5-cf806d102fba",
                "HostIP": "172.16.51.209",
                "HostName": "harborV2_yancyw",
                "HostStatus": "ONLINE",
                "JoinState": true,
                "PublicIP": "139.199.178.171"
            }
        ],
        "RangeType": 1,
        "RequestId": "a38b89a7-fbdf-4133-9981-1c09a5a94895",
        "TotalCount": 55
    }
}
```

