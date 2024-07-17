**Example 1: 拉取prometheus配置**

拉取prometheus配置

Input: 

```
tccli monitor DescribePrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --ClusterType tke \
    --ClusterId cls-xxx
```

Output: 
```
{
    "Response": {
        "Config": "abc",
        "ServiceMonitors": [
            {
                "Name": "test-sm",
                "Config": "scrape_interval:5s\n",
                "TemplateId": "temp-akdj",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "PodMonitors": [
            {
                "Name": "test-pm",
                "Config": "scrape_interval:5s\n",
                "TemplateId": "temp-akdj",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "RawJobs": [
            {
                "Name": "test-rawjob",
                "Config": "scrape_interval:5s\n",
                "TemplateId": "temp-akdj",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "Probes": [
            {
                "Name": "test-probe",
                "Config": "scrape_interval:5s\n",
                "TemplateId": "temp-akdj",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "ImageNeedUpdate": true,
        "RequestId": "abc"
    }
}
```

