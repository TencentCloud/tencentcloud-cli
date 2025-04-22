**Example 1: 【监控】获取巡检任务结果列表**



Input: 

```
tccli emr DescribeInspectionTaskResult --cli-unfold-argument  \
    --InstanceId emr-nwb7sg2o \
    --StartTime 1589900474 \
    --EndTime 1589910630
```

Output: 
```
{
    "Response": {
        "InspectionResultInfo": "W3siSWQiOiI5MDciLCJUaW1lIjoiMjAyNS0wNC0xNSAxNTozNzo1NyIsIk5hbWUiOiJlbXItbXd5aXh3eHBfMjAyNTA0MTVfMTUzNzU3LnBkZiIsIlR5cGUiOiLljbPml7YiLCJTdGF0dXMiOiLmiqXlkYrnlJ/miJDkuK0iLCJMaW5rIjoiLSIsIk9uTGluZVN0YXR1cyI6MX0seyJJZCI6IjkwNiIsIlRpbWUiOiIyMDI1LTA0LTE1IDE1OjAzOjU0IiwiTmFtZSI6ImVtci1td3lpeHd4cF8yMDI1MDQxNV8xNTAzNTQucGRmIiwiVHlwZSI6IuWNs+aXtiIsIlN0YXR1cyI6IuW3sueUn+aIkCIsIkxpbmsiOiJodHRwczovL2Vtcy1pbnNwZWN0aW9uLXJlcG9ydC1jcS0xMjU5MzUzMzQzLmNvcy5hcC1jaG9uZ3FpbmcubXlxY2xvdWQuY29tL2NxL2Vtci1td3lpeHd4cC9lbXItbXd5aXh3eHBfMjAyNTA0MTVfMTUwMzU0LnBkZj9xLXNpZ24tYWxnb3JpdGhtPXNoYTFcdTAwMjZxLWFrPUFLSUR5bEliamJDWGJPdFk5Wm9mSmwxM3JVd0FOQ3FIWGxuWlx1MDAyNnEtc2lnbi10aW1lPTE3NDQ3MDA3MDMlM0IxNzYwNzcxMTAzXHUwMDI2cS1rZXktdGltZT0xNzQ0NzAwNzAzJTNCMTc2MDc3MTEwM1x1MDAyNnEtaGVhZGVyLWxpc3Q9aG9zdFx1MDAyNnEtdXJsLXBhcmFtLWxpc3Q9XHUwMDI2cS1zaWduYXR1cmU9NDcwZGQyNzlmYjg1OTE3MzliYTdkYmYzNDhjOTZlNWZlOWRmMzM0NSIsIk9uTGluZVN0YXR1cyI6Mn1d",
        "RequestId": "fd0ea005-5d84-4d21-ac87-8e02f7910795",
        "Total": 2,
        "TypeInfo": "eyJGaXhlZFRpbWUiOiLlrprml7YiLCJSZWFsVGltZSI6IuWNs+aXtiJ9"
    }
}
```

