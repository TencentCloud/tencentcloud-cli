**Example 1: CreateTimeTemplate**



Input: 

```
tccli iotvideoindustry CreateTimeTemplate --cli-unfold-argument  \
    --IsAllWeek 0 \
    --TimeTemplateSpecs.0.DayofWeek 1 \
    --TimeTemplateSpecs.0.EndTime 12:30 \
    --TimeTemplateSpecs.0.BeginTime 14:30 \
    --Name myTemplate
```

Output: 
```
{
    "Response": {
        "RequestId": "e1b9e7ac-0989-4af9-a454-26f69d6997d9",
        "TemplateId": "template-xxx"
    }
}
```

