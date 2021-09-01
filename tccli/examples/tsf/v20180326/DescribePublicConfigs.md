**Example 1: 查询公共配置项列表**



Input: 

```
tccli tsf DescribePublicConfigs --cli-unfold-argument  \
    --ConfigName global \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "79839cba-fda2-4e2c-9dfa-88f8492db608",
        "Result": {
            "TotalCount": 6,
            "Content": [
                {
                    "ConfigId": "dcfg-p-byx6nkyl",
                    "ConfigName": "global",
                    "ConfigVersion": "1.1",
                    "ConfigVersionDesc": "增加默认hystrix超时设置",
                    "ConfigValue": "management:\r\n  health:\r\n    consul:\r\n      enabled: false\r\n  endpoint:\r\n    health:\r\n      show-details: always\r\n\r\nhystrix:\r\n  command:\r\n    default:\r\n      execution:\r\n        timeout:\r\n          enabled: true\r\n        isolation:\r\n          thread:\r\n            timeoutInMilliseconds: 30000\r\n\r\nribbon:\r\n  ReadTimeout: 30000\r\n  ConnectTimeout: 30000        ",
                    "CreationTime": "2019-05-13 10:01:14",
                    "LastUpdateTime": null,
                    "ConfigVersionCount": null,
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "DeleteFlag": true,
                    "ConfigType": null
                },
                {
                    "ConfigId": "dcfg-p-nygnkbv2",
                    "ConfigName": "global",
                    "ConfigVersion": "1.5",
                    "ConfigVersionDesc": "调整ribbon重试",
                    "ConfigValue": "management:\r\n  health:\r\n    consul:\r\n      enabled: false\r\n  endpoint:\r\n    health:\r\n      show-details: always\r\n\r\nhystrix:\r\n  command:\r\n    default:\r\n      execution:\r\n        timeout:\r\n          enabled: true\r\n        isolation:\r\n          thread:\r\n            timeoutInMilliseconds: 30000\r\n\r\nribbon:\r\n  MaxAutoRetries: 0\r\n  MaxAutoRetriesNextServer: 1\r\n  ReadTimeout: 15000\r\n  ConnectTimeout: 3000        \r\n\r\nfeign:\r\n  hystrix:\r\n    enabled: true\r\n  client:\r\n    config:\r\n      default:\r\n        c",
                    "CreationTime": "2019-05-22 10:48:05",
                    "LastUpdateTime": null,
                    "ConfigVersionCount": null,
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "DeleteFlag": true,
                    "ConfigType": null
                },
                {
                    "ConfigId": "dcfg-p-py53d6v4",
                    "ConfigName": "global",
                    "ConfigVersion": "1.9",
                    "ConfigVersionDesc": "调整ribbon超时设置",
                    "ConfigValue": "management:\r\n  health:\r\n    consul:\r\n      enabled: false\r\n  endpoint:\r\n    health:\r\n      show-details: always\r\n\r\nhystrix:\r\n  command:\r\n    default:\r\n      execution:\r\n        timeout:\r\n          enabled: true\r\n        isolation:\r\n          thread:\r\n            timeoutInMilliseconds: 3000\r\n\r\nribbon:\r\n  MaxAutoRetries: 0\r\n  MaxAutoRetriesNextServer: 1\r\n  ReadTimeout: 8000\r\n  ConnectTimeout: 3000        \r\n\r\nfeign:\r\n  hystrix:\r\n    enabled: true\r\n  client:\r\n    config:\r\n      default:\r\n        con",
                    "CreationTime": "2019-05-23 23:04:54",
                    "LastUpdateTime": null,
                    "ConfigVersionCount": null,
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "DeleteFlag": true,
                    "ConfigType": null
                },
                {
                    "ConfigId": "dcfg-p-dap7g3ao",
                    "ConfigName": "global",
                    "ConfigVersion": "2.3",
                    "ConfigVersionDesc": "调整默认hystrix线程池设置",
                    "ConfigValue": "management:\r\n  health:\r\n    consul:\r\n      enabled: false\r\n  endpoint:\r\n    health:\r\n      show-details: always\r\n\r\nhystrix:\r\n  threadpool:\r\n    default:\r\n      coreSize: 400\r\n      maximumSize: 400\r\n  command:\r\n    default:\r\n      execution:\r\n        timeout:\r\n          enabled: true\r\n        isolation:\r\n          thread:\r\n            timeoutInMilliseconds: 3000\r\n\r\nribbon:\r\n  MaxAutoRetries: 0\r\n  MaxAutoRetriesNextServer: 1\r\n  ReadTimeout: 8000\r\n  ConnectTimeout: 3000        \r\n\r\nfeign:\r\n  hystri",
                    "CreationTime": "2019-05-24 16:39:59",
                    "LastUpdateTime": null,
                    "ConfigVersionCount": null,
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "DeleteFlag": false,
                    "ConfigType": null
                },
                {
                    "ConfigId": "dcfg-p-zvwgl6y8",
                    "ConfigName": "global",
                    "ConfigVersion": "2.4",
                    "ConfigVersionDesc": "调整默认hystrix线程池设置",
                    "ConfigValue": "management:\r\n  health:\r\n    consul:\r\n      enabled: false\r\n  endpoint:\r\n    health:\r\n      show-details: always\r\n\r\nhystrix:\r\n  threadpool:\r\n    default:\r\n      coreSize: 30\r\n      maximumSize: 30\r\n  command:\r\n    default:\r\n      execution:\r\n        timeout:\r\n          enabled: true\r\n        isolation:\r\n          thread:\r\n            timeoutInMilliseconds: 3000\r\n\r\nribbon:\r\n  MaxAutoRetries: 0\r\n  MaxAutoRetriesNextServer: 1\r\n  ReadTimeout: 8000\r\n  ConnectTimeout: 3000        \r\n\r\nfeign:\r\n  hystrix:",
                    "CreationTime": "2019-05-24 18:30:35",
                    "LastUpdateTime": null,
                    "ConfigVersionCount": null,
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "DeleteFlag": true,
                    "ConfigType": null
                },
                {
                    "ConfigId": "dcfg-p-nalgo4yq",
                    "ConfigName": "global",
                    "ConfigVersion": "no.hystrix.test",
                    "ConfigVersionDesc": "no-hystrix-test",
                    "ConfigValue": "management:\r\n  health:\r\n    consul:\r\n      enabled: false\r\n  endpoint:\r\n    health:\r\n      show-details: always\r\n\r\nribbon:\r\n  MaxAutoRetries: 0\r\n  MaxAutoRetriesNextServer: 1\r\n  ReadTimeout: 8000\r\n  ConnectTimeout: 3000        ",
                    "CreationTime": "2019-05-24 20:39:12",
                    "LastUpdateTime": null,
                    "ConfigVersionCount": null,
                    "ApplicationId": null,
                    "ApplicationName": null,
                    "DeleteFlag": true,
                    "ConfigType": null
                }
            ]
        }
    }
}
```

