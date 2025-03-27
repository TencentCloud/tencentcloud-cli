**Example 1: 获得实例级别监控配置**

获得实例级别监控配置

Input: 

```
tccli monitor DescribePrometheusGlobalConfig --cli-unfold-argument  \
    --InstanceId prom-abcd
```

Output: 
```
{
    "Response": {
        "Config": "global:\n  scrape_interval: 15s \n  evaluation_interval: 15s \nscrape_configs:\n  - job_name: \"prometheus\"\n    static_configs:\n      - targets: [\"localhost:9090\"]",
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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

