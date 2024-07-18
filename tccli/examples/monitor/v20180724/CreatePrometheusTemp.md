**Example 1: 创建一个模板**

创建一个模板

Input: 

```
tccli monitor CreatePrometheusTemp --cli-unfold-argument  \
    --Template.Name t1 \
    --Template.Describe 一个模板 \
    --Template.ServiceMonitors.0.Name s \
    --Template.ServiceMonitors.0.Config abc \
    --Template.Level 'cluster


{
  "Template": {
        "Name": "test",
        "Describe": "test",
        "Level": "instance",
        "RecordRules": [
          {
            "Name": "testRule",
            "Config": "abc",
            "TemplateId": "temp-asdj",
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
            "Name": "abc",
            "Config": "abc",
            "TemplateId": "abc",
            "Targets": {
              "Total": 1,
              "Up": 1,
              "Down": 1,
              "Unknown": 1
            }
          }
        ],
        "ServiceMonitors": [
          {
             "Name": "test-sm",
            "Config": "abc",
            "TemplateId": "temp-asdj",
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
            "Config": "abc",
            "TemplateId": "temp-asdj",
            "Targets": {
              "Total": 1,
              "Up": 1,
              "Down": 1,
              "Unknown": 1
            }
          }
        ],
        "TemplateId": "temp-asdj",
        "UpdateTime": "2024-07-16T08:28:54Z",
        "Version": "v1",
        "IsDefault": true,
        "AlertDetailRules": [
          {
            "Id": "rule-asdk",
            "Name": "testAlert",
            "TemplateId": "temp-asdj",
            "Notification": {
              "Enabled": true,
              "Type": "amp",
              "WebHook": "abc",
              "AlertManager": {
                "ClusterType": "tke",
                "ClusterId": "cls-askj",
                "Url": "http://asasdkfh:9000"
              },
              "RepeatInterval": "5m",
              "TimeRangeStart": "00:00:00",
              "TimeRangeEnd": "23:59:59",
              "NotifyWay": [
                "abc"
              ],
              "ReceiverGroups": [
                "notice-yakj"
              ],
              "PhoneNotifyOrder": [
                1
              ],
              "PhoneCircleTimes": 0,
              "PhoneInnerInterval": 0,
              "PhoneCircleInterval": 0,
              "PhoneArriveNotice": true
            },
            "Rules": [
              {
                "Name": "rule-ajdb",
                "Rule": "avg by (abc) skdj",
                "Labels": [
                  {
                    "Name": "label-name",
                    "Value": "label-value"
                  }
                ],
                "Template": "temp-asdj",
                "For": "5m",
                "Describe": "test-temp",
                "Annotations": [
                  {
                    "Name": "label-name",
                    "Value": "label-value"
                  }
                ],
                "RuleState": 0
              }
            ],
            "UpdatedAt": "2024-07-16 16:28:54",
            "ClusterId": "cls-djfb",
            "Interval": "5m"
          }
        ],
        "TargetsTotal": 0
      }
}'
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "TemplateId": "temp-lejrh"
    }
}
```

