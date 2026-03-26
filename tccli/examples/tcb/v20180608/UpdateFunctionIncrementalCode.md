**Example 1: 增量更新函数代码**

增量更新函数代码

Input: 

```
tccli tcb UpdateFunctionIncrementalCode --cli-unfold-argument  \
    --FunctionName scfweb \
    --EnvId low-scf-web \
    --Namespace low-scf-web \
    --AddFiles UEsDBAoAAAAAAMh1ik0grgrjGQAAABkAAAAFAAAAYWEucHlkZWYgZigpOgoJcmV0dXJuICdoZWxsbycKUEsBAj8ACgAAAAAAyHWKTSCuCuMZAAAAGQAAAAUAJAAAAAAAAAAgAAAAAAAAAGFhLnB5CgAgAAAAAAABABgA8fbxC1SQ1AGylvML2I3UAbKW8wvYjdQBUEsFBgAAAAABAAEAVwAAADwAAAAAAA \
    --DeleteFiles pkg/file1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

