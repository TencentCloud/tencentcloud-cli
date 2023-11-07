**Example 1: 获取流量监控信息**

获取流量监控信息

Input: 

```
tccli mna GetNetMonitor --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MonitorData": [
            {
                "Time": "1673601780",
                "BusinessMetrics": 492350276.319998,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 27582845.919998
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 395158790.239997
                    }
                ]
            },
            {
                "Time": "1673601840",
                "BusinessMetrics": 412655416,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 27228367.066665
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 397505721.866666
                    }
                ]
            },
            {
                "Time": "1673601900",
                "BusinessMetrics": 411823866.666665,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 28047154.266665
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 396059005.333333
                    }
                ]
            },
            {
                "Time": "1673601960",
                "BusinessMetrics": 412108687.733331,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 29244132.933331
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 395156858.266664
                    }
                ]
            },
            {
                "Time": "1673602020",
                "BusinessMetrics": 412778279.866666,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 26898350.666666
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 398191465.733331
                    }
                ]
            },
            {
                "Time": "1673602080",
                "BusinessMetrics": 412630582.533333,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 28580784.266665
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 396357362.933332
                    }
                ]
            },
            {
                "Time": "1673602140",
                "BusinessMetrics": 412431913.466665,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 27329174.8
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 397404181.866666
                    }
                ]
            },
            {
                "Time": "1673602200",
                "BusinessMetrics": 410982346.266665,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 29038580.399999
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 394201611.866666
                    }
                ]
            },
            {
                "Time": "1673602260",
                "BusinessMetrics": 409923330.933332,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 28212205.599999
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 393937825.066666
                    }
                ]
            },
            {
                "Time": "1673602320",
                "BusinessMetrics": 353662726.399999,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": 25376171.542857
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": 338834939.199999
                    }
                ]
            },
            {
                "Time": "1673602380",
                "BusinessMetrics": -1,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": -1
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": -1
                    }
                ]
            },
            {
                "Time": "1673602440",
                "BusinessMetrics": -1,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": -1
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": -1
                    }
                ]
            },
            {
                "Time": "1673602500",
                "BusinessMetrics": -1,
                "SlotNetInfo": [
                    {
                        "NetInfoName": "eth0",
                        "PublicIP": "9.223.110.232",
                        "Current": -1
                    },
                    {
                        "NetInfoName": "eth1",
                        "PublicIP": "9.223.96.218",
                        "Current": -1
                    }
                ]
            }
        ],
        "RequestId": "xxx"
    }
}
```

