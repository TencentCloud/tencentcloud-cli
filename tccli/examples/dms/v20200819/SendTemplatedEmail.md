**Example 1: Sending template emails**



Input: 

```
tccli dms SendTemplatedEmail --cli-unfold-argument  \
    --FromAddress test@example.com \
    --ToAddress to@example.com \
    --TemplateName templateName1 \
    --TemplateValue templateValue1
```

Output: 
```
{
    "result": true
}
```

