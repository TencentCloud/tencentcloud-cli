**Example 1: 根据经验模板创建演练**

通过预创建好的经验模板生成常规化的演练持续使用

Input: 

```
tccli cfg CreateTaskFromTemplate --cli-unfold-argument  \
    --TemplateId 689 \
    --TaskConfig.TaskTitle 测试演练，关联了实例，修改了演练名称和第一个动作组中第一个动作的动作自定义参数 \
    --TaskConfig.TaskGroupsConfig.0.TaskGroupInstances ins-xxxxxxxx \
    --TaskConfig.TaskGroupsConfig.0.TaskGroupActionsConfig.0.TaskGroupActionOrder 1 \
    --TaskConfig.TaskGroupsConfig.0.TaskGroupActionsConfig.0.TaskGroupActionCustomConfiguration {"timeout":200,"percentage":80}
```

Output: 
```
{
    "Response": {
        "RequestId": "f0aee8ac-2ed3-4a7f-a25b-f0d7d228dd30",
        "TaskId": 50
    }
}
```

