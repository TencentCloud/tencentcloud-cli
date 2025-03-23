**Example 1: 修改规则引擎优先级**

站点下有 3 条规则，原来执行顺序是 rule-example1、rule-example2、rule-example3，需要修改成执行顺序是 rule-example2、rule-example3、rule-example1。

Input: 

```
tccli teo ModifyL7AccRulePriority --cli-unfold-argument  \
    --ZoneId zone-example \
    --RuleIds rule-example2 rule-example3 rule-example1
```

Output: 
```
{
    "Response": {
        "RequestId": "example-310c-41f4-b5e7-abe407404sxsd"
    }
}
```

