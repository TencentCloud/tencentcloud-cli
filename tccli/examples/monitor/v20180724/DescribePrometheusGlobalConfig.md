**Example 1: 获得实例级别监控配置**

获得实例级别监控配置

Input: 

```
tccli monitor DescribePrometheusGlobalConfig --cli-unfold-argument  \
    --InstanceId prom-xxx
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
        "RequestId": "abc"
    }
}
```

