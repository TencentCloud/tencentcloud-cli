**Example 1: 查询web服务列表**



Input: 

```
tccli tcss DescribeAssetWebServiceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ServiceID": "616334633131363739616263383435663365306465666135646234656634363731323536323939383433",
                "HostID": "33f4b57c-2b0c-4643-9aee-93f90a2d63b5",
                "HostIP": "10.0.0.3",
                "ContainerName": "/p1",
                "MainType": "web",
                "Type": "Apache",
                "Version": "2.4.38",
                "RunAs": "root:root",
                "Exe": "/usr/sbin/apache2",
                "Config": "/etc/apache2/apache2.conf",
                "ProcessCnt": 0,
                "AccessLog": "",
                "ErrorLog": "",
                "DataPath": "",
                "WebRoot": "",
                "Pids": [
                    1882552,
                    1883015,
                    1883016,
                    1883017,
                    1883018,
                    1883019
                ],
                "Listen": [
                    "tcp://0.0.0.0:80"
                ],
                "Parameter": "apache2 -DFOREGROUND",
                "ContainerId": "d591c50bbcd79bb3f45d661c0a1864102aaa5fa577a69a67a546d8380956dc04"
            }
        ],
        "RequestId": "48ca3c70-801e-48b1-80a7-1007afbf5ffb",
        "TotalCount": 7
    }
}
```

