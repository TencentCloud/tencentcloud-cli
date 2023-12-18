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
    "Name": "abc",
    "Describe": "abc",
    "Level": "abc",
    "RecordRules": [
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
    "PodMonitors": [
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
    "TemplateId": "abc",
    "UpdateTime": "abc",
    "Version": "abc",
    "IsDefault": true,
    "AlertDetailRules": [
      {
        "Id": "abc",
        "Name": "abc",
        "TemplateId": "abc",
        "Notification": {
          "Enabled": true,
          "Type": "abc",
          "WebHook": "abc",
          "AlertManager": {
            "ClusterType": "abc",
            "ClusterId": "abc",
            "Url": "abc"
          },
          "RepeatInterval": "abc",
          "TimeRangeStart": "abc",
          "TimeRangeEnd": "abc",
          "NotifyWay": [
            "abc"
          ],
          "ReceiverGroups": [
            "abc"
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
            "Name": "abc",
            "Rule": "abc",
            "Labels": [
              {
                "Name": "abc",
                "Value": "abc"
              }
            ],
            "Template": "abc",
            "For": "abc",
            "Describe": "abc",
            "Annotations": [
              {
                "Name": "abc",
                "Value": "abc"
              }
            ],
            "RuleState": 0
          }
        ],
        "UpdatedAt": "abc",
        "ClusterId": "abc",
        "Interval": "abc"
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
        "TemplateId": "temp-xxx"
    }
}
```

