**Example 1: 获取指标主题的采集配置**



Input: 

```
tccli cls DescribeTopicMetricConfigs --cli-unfold-argument  \
    --TopicId d7adf66d-88a7-4321-8b4b-6f2c7a9773b8 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Datas": [
            {
                "ConfigId": "1bfadff7-9c5d-48c2-b985-21670d9d007e",
                "CreateTime": 1724308693,
                "Flag": 1,
                "GroupIds": [
                    "886bf7a8-7340-4314-8d64-b360da0ffd78"
                ],
                "HonorLabels": false,
                "Name": "test-test",
                "Operate": 0,
                "Scheme": "",
                "ScrapeInterval": "",
                "ScrapeTimeout": "",
                "Source": 0,
                "TopicIds": [
                    "d7adf66d-88a7-4321-8b4b-6f2c7a9773b8"
                ],
                "Type": 1,
                "UpdateTime": 1724308693,
                "YamlSpec": {
                    "Spec": "typemeta:\n  kind: ServiceMonitor\n  apiversion: monitoring.coreos.com/v1\nobjectmeta:\n  name: test-test\n  generatename: \"\"\n  namespace: test\n  selflink: \"\"\n  uid: \"\"\n  resourceversion: \"\"\n  generation: 0\n  creationtimestamp: \"0001-01-01T00:00:00Z\"\n  deletiontimestamp: null\n  deletiongraceperiodseconds: null\n  labels: {}\n  annotations: {}\n  ownerreferences: []\n  finalizers: []\n  managedfields: []\nspec:\n  joblabel: \"\"\n  targetlabels: []\n  podtargetlabels: []\n  endpoints:\n  - port: 8080-8080-tcp\n    targetport: null\n    path: /metrics\n    scheme: \"\"\n    params: {}\n    interval: 15s\n    scrapetimeout: \"\"\n    tlsconfig: null\n    bearertokenfile: \"\"\n    bearertokensecret: null\n    authorization: null\n    honorlabels: false\n    honortimestamps: null\n    tracktimestampsstaleness: null\n    basicauth: null\n    oauth2: null\n    metricrelabelconfigs: []\n    relabelconfigs:\n    - sourcelabels:\n      - __meta_kubernetes_pod_label_app\n      separator: null\n      targetlabel: application\n      regex: \"\"\n      modulus: 0\n      replacement: null\n      action: replace\n    proxyurl: null\n    followredirects: null\n    enablehttp2: null\n    filterrunning: null\n  selector:\n    matchlabels:\n      app: test\n    matchexpressions: []\n  namespaceselector:\n    any: false\n    matchnames:\n    - test\n  samplelimit: null\n  scrapeprotocols: []\n  targetlimit: null\n  labellimit: null\n  labelnamelengthlimit: null\n  labelvaluelengthlimit: null\n  keepdroppedtargets: null\n  attachmetadata: null\n  scrapeclassname: null\n  bodysizelimit: null\n",
                    "Type": "ServiceMonitor"
                }
            },
            {
                "ConfigId": "fd6dced0-5cc1-4d81-b0d3-c42ee56842cd",
                "CreateTime": 1723640091,
                "Flag": 0,
                "GroupIds": [
                    "886bf7a8-7340-4314-8d64-b360da0ffd78"
                ],
                "HonorLabels": false,
                "MetricLabel": {
                    "CustomLabels": [],
                    "Label": {
                        "Keys": [],
                        "Type": 0
                    },
                    "Metadata": [
                        "namespace",
                        "pod_name",
                        "pod_ip",
                        "pod_uid",
                        "container_name",
                        "container_id",
                        "image_name"
                    ]
                },
                "Name": "test1",
                "Operate": 0,
                "Scheme": "http",
                "ScrapeInterval": "60s",
                "ScrapeTimeout": "30s",
                "Source": 0,
                "Spec": {
                    "CustomSpecs": [
                        {
                            "Namespaces": [
                                ""
                            ],
                            "Path": "/erq",
                            "PodLabel": [
                                {
                                    "Key": "ab",
                                    "Operate": "=",
                                    "Values": [
                                        "em",
                                        "q"
                                    ]
                                }
                            ],
                            "Port": "8080"
                        }
                    ]
                },
                "TopicIds": [
                    "d7adf66d-88a7-4321-8b4b-6f2c7a9773b8"
                ],
                "Type": 1,
                "UpdateTime": 1723709068
            }
        ],
        "RequestId": "a725cc9c-2de7-4180-b1dc-b4bae8a79707",
        "TotalCount": 2
    }
}
```

