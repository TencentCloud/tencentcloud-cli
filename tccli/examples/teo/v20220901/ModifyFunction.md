**Example 1: 修改边缘函数**



Input: 

```
tccli teo ModifyFunction --cli-unfold-argument  \
    --ZoneId zone-2gqxim9jstab \
    --FunctionId ef-1pakhnuy \
    --Remark my function \
    --Content addEventListener('fetch', e => {
  const response = new Response('Hello World!');
  e.respondWith(response);
});
```

Output: 
```
{
    "Response": {
        "RequestId": "b660855b-a0a7-4cd3-832d-e01fb1b8da93"
    }
}
```

