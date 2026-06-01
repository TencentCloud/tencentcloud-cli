**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeEngineExtParams --cli-unfold-argument  \
    --Product tchouse-x
```

Output: 
```
{
    "Response": {
        "ExtParams": [
            {
                "Description": "主类(Main Class)程序包为jar类型则必填",
                "Name": "ClassName",
                "Type": "input",
                "UIComponentConfigs": "eyJpbnB1dCI6eyJtYXhsZW5ndGgiOjMwMCwicGxhY2Vob2xkZXIiOiIifX0="
            },
            {
                "Description": "依赖的jar仅支持 jar 格式文件，可配置多个",
                "Name": "Jars",
                "Type": "input",
                "UIComponentConfigs": "eyJpbnB1dCI6eyJtYXhsZW5ndGgiOjEwMDAsInBsYWNlaG9sZGVyIjoiIn19"
            },
            {
                "Description": "--config key=value配置属性,一行一个,\\n分隔",
                "Name": "Conf",
                "Type": "input",
                "UIComponentConfigs": "eyJpbnB1dCI6eyJtYXhsZW5ndGgiOjEwMDAsInBsYWNlaG9sZGVyIjoiIn19"
            },
            {
                "Description": "--files 依赖Files资源,多个用逗号分隔",
                "Name": "Files",
                "Type": "input",
                "UIComponentConfigs": "eyJpbnB1dCI6eyJtYXhsZW5ndGgiOjEwMDAsInBsYWNlaG9sZGVyIjoiIn19"
            },
            {
                "Description": "--archives 仅支持 gz、tgz、tar 格式文件，可配置多个,逗号分隔",
                "Name": "Archives",
                "Type": "input",
                "UIComponentConfigs": "eyJpbnB1dCI6eyJtYXhsZW5ndGgiOjEwMDAsInBsYWNlaG9sZGVyIjoiIn19"
            }
        ],
        "RequestId": "e38df29d-0aff-4d45-b0ed-2e36f26cd06f"
    }
}
```

