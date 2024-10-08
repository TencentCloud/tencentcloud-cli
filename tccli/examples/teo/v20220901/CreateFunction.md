**Example 1: 创建函数**



Input: 

```
tccli teo CreateFunction --cli-unfold-argument  \
    --ZoneId zone-293e7s5jne1i \
    --Name test-function \
    --Remark my test function \
    --Content addEventListener('fetch', e => {
  const response = new Response('Hello World!');
  e.respondWith(response);
});
```

Output: 
```
{
    "Response": {
        "FunctionId": "ef-1pakhnuy",
        "RequestId": "85caed2d-e16e-4205-a322-1e907e830b55"
    }
}
```

