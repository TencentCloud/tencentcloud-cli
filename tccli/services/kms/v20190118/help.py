# -*- coding: utf-8 -*-
DESC = "kms-2019-01-18"
INFO = {
  "DeleteImportedKeyMaterial": {
    "params": [
      {
        "name": "KeyId",
        "desc": "指定需要删除密钥材料的EXTERNAL CMK。"
      }
    ],
    "desc": "用于删除导入的密钥材料，仅对EXTERNAL类型的CMK有效，该接口将CMK设置为PendingImport 状态，并不会删除CMK，在重新进行密钥导入后可继续使用。彻底删除CMK请使用 ScheduleKeyDeletion 接口。"
  },
  "Encrypt": {
    "params": [
      {
        "name": "KeyId",
        "desc": "调用CreateKey生成的CMK全局唯一标识符"
      },
      {
        "name": "Plaintext",
        "desc": "被加密的明文数据，该字段必须使用base64编码，原文最大长度支持4K"
      },
      {
        "name": "EncryptionContext",
        "desc": "key/value对的json字符串，如果指定了该参数，则在调用Decrypt API时需要提供同样的参数，最大支持1024个字符"
      }
    ],
    "desc": "本接口用于加密最多为4KB任意数据，可用于加密数据库密码，RSA Key，或其它较小的敏感信息。对于应用的数据加密，使用GenerateDataKey生成的DataKey进行本地数据的加解密操作"
  },
  "EnableWhiteBoxKeys": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "白盒密钥的全局唯一标识符列表。注意：要确保所有提供的KeyId是格式有效的，没有重复，个数不超过50个，并且都是有效存在的。"
      }
    ],
    "desc": "批量启用白盒密钥"
  },
  "UpdateAlias": {
    "params": [
      {
        "name": "Alias",
        "desc": "新的别名，1-60个字符或数字的组合"
      },
      {
        "name": "KeyId",
        "desc": "CMK的全局唯一标识符"
      }
    ],
    "desc": "用于修改CMK的别名。对于处于PendingDelete状态的CMK禁止修改。"
  },
  "DeleteWhiteBoxKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "白盒密钥的全局唯一标识符"
      }
    ],
    "desc": "删除白盒密钥, 注意：必须先禁用后，才可以删除。"
  },
  "ImportKeyMaterial": {
    "params": [
      {
        "name": "EncryptedKeyMaterial",
        "desc": "使用GetParametersForImport 返回的PublicKey加密后的密钥材料base64编码。对于国密版本region的KMS，导入的密钥材料长度要求为 128 bit，FIPS版本region的KMS， 导入的密钥材料长度要求为 256 bit。"
      },
      {
        "name": "ImportToken",
        "desc": "通过调用GetParametersForImport获得的导入令牌。"
      },
      {
        "name": "KeyId",
        "desc": "指定导入密钥材料的CMK，需要和GetParametersForImport 指定的CMK相同。"
      },
      {
        "name": "ValidTo",
        "desc": "密钥材料过期时间 unix 时间戳，不指定或者 0 表示密钥材料不会过期，若指定过期时间，需要大于当前时间点，最大支持 2147443200。"
      }
    ],
    "desc": "用于导入密钥材料。只有类型为EXTERNAL 的CMK 才可以导入，导入的密钥材料使用 GetParametersForImport 获取的密钥进行加密。可以为指定的 CMK 重新导入密钥材料，并重新指定过期时间，但必须导入相同的密钥材料。CMK 密钥材料导入后不可以更换密钥材料。导入的密钥材料过期或者被删除后，指定的CMK将无法使用，需要再次导入相同的密钥材料才能正常使用。CMK是独立的，同样的密钥材料可导入不同的 CMK 中，但使用其中一个 CMK 加密的数据无法使用另一个 CMK解密。\n只有Enabled 和 PendingImport状态的CMK可以导入密钥材料。"
  },
  "GetPublicKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK的唯一标识。"
      }
    ],
    "desc": "该接口用户获取 KeyUsage为ASYMMETRIC_DECRYPT_RSA_2048 和 ASYMMETRIC_DECRYPT_SM2 的非对称密钥的公钥信息，使用该公钥用户可在本地进行数据加密，使用该公钥加密的数据只能通过KMS使用对应的私钥进行解密。只有处于Enabled状态的非对称密钥才可能获取公钥。"
  },
  "DisableKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK唯一标识符"
      }
    ],
    "desc": "本接口用于禁用一个主密钥，处于禁用状态的Key无法用于加密、解密操作。"
  },
  "GenerateDataKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK全局唯一标识符"
      },
      {
        "name": "KeySpec",
        "desc": "指定生成Datakey的加密算法以及Datakey大小，AES_128或者AES_256。KeySpec 和 NumberOfBytes 必须指定一个"
      },
      {
        "name": "NumberOfBytes",
        "desc": "生成的DataKey的长度，同时指定NumberOfBytes和KeySpec时，以NumberOfBytes为准。最小值为1， 最大值为1024。KeySpec 和 NumberOfBytes 必须指定一个"
      },
      {
        "name": "EncryptionContext",
        "desc": "key/value对的json字符串，如果使用该字段，则返回的DataKey在解密时需要填入相同的字符串"
      }
    ],
    "desc": "本接口生成一个数据密钥，您可以用这个密钥进行本地数据的加密。"
  },
  "AsymmetricSm2Decrypt": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK的唯一标识"
      },
      {
        "name": "Ciphertext",
        "desc": "使用PublicKey加密的密文，Base64编码。密文长度不能超过256字节。"
      }
    ],
    "desc": "使用指定的SM2非对称密钥的私钥进行数据解密，密文必须是使用对应公钥加密的。处于Enabled 状态的非对称密钥才能进行解密操作。传入的密文的长度不能超过256字节。"
  },
  "CancelKeyDeletion": {
    "params": [
      {
        "name": "KeyId",
        "desc": "需要被取消删除的CMK的唯一标志"
      }
    ],
    "desc": "取消CMK的计划删除操作"
  },
  "GetKeyRotationStatus": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK唯一标识符"
      }
    ],
    "desc": "查询指定的CMK是否开启了密钥轮换功能。"
  },
  "DescribeWhiteBoxKeyDetails": {
    "params": [
      {
        "name": "KeyStatus",
        "desc": "过滤条件：密钥的状态，0：disabled，1：enabled"
      }
    ],
    "desc": "获取白盒密钥列表"
  },
  "DisableKeys": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "需要批量禁用的CMK Id 列表，CMK数量最大支持100"
      }
    ],
    "desc": "该接口用于批量禁止CMK的使用。"
  },
  "EncryptByWhiteBox": {
    "params": [
      {
        "name": "KeyId",
        "desc": "白盒密钥的全局唯一标识符"
      },
      {
        "name": "PlainText",
        "desc": "待加密的文本， base64编码，文本的原始长度最大不超过4KB"
      },
      {
        "name": "InitializationVector",
        "desc": "初始化向量，大小为 16 Bytes，加密算法会使用到, base64编码；如果不传，则由后端服务随机生成。用户需要自行保存该值，作为解密的参数。"
      }
    ],
    "desc": "使用白盒密钥进行加密"
  },
  "ListAlgorithms": {
    "params": [],
    "desc": "列出当前Region支持的加密方式"
  },
  "ReEncrypt": {
    "params": [
      {
        "name": "CiphertextBlob",
        "desc": "需要重新加密的密文"
      },
      {
        "name": "DestinationKeyId",
        "desc": "重新加密使用的CMK，如果为空，则使用密文原有的CMK重新加密（若密钥没有轮换则密文不会刷新）"
      },
      {
        "name": "SourceEncryptionContext",
        "desc": "CiphertextBlob 密文加密时使用的key/value对的json字符串。如果加密时未使用，则为空"
      },
      {
        "name": "DestinationEncryptionContext",
        "desc": "重新加密使用的key/value对的json字符串，如果使用该字段，则返回的新密文在解密时需要填入相同的字符串"
      }
    ],
    "desc": "使用指定CMK对密文重新加密。"
  },
  "ListKeys": {
    "params": [
      {
        "name": "Offset",
        "desc": "含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0"
      },
      {
        "name": "Limit",
        "desc": "含义跟 SQL 查询的 Limit 一致，表示本次获最多获取 Limit 个元素。缺省值为10，最大值为200"
      },
      {
        "name": "Role",
        "desc": "根据创建者角色筛选，默认 0 表示用户自己创建的cmk， 1 表示授权其它云产品自动创建的cmk"
      }
    ],
    "desc": "列出账号下面状态为Enabled， Disabled 和 PendingImport 的CMK KeyId 列表"
  },
  "GenerateRandom": {
    "params": [
      {
        "name": "NumberOfBytes",
        "desc": "生成的随机数的长度。最小值为1， 最大值为1024。"
      }
    ],
    "desc": "随机数生成接口。"
  },
  "CreateKey": {
    "params": [
      {
        "name": "Alias",
        "desc": "作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字母数字 - _ 的组合，首字符必须为字母或者数字。以 kms- 作为前缀的用于云产品使用，Alias 不可重复。"
      },
      {
        "name": "Description",
        "desc": "CMK 的描述，最大1024字节"
      },
      {
        "name": "KeyUsage",
        "desc": "指定key的用途，默认为  \"ENCRYPT_DECRYPT\" 表示创建对称加解密密钥，其它支持用途 “ASYMMETRIC_DECRYPT_RSA_2048” 表示创建用于加解密的RSA2048非对称密钥，“ASYMMETRIC_DECRYPT_SM2” 表示创建用于加解密的SM2非对称密钥"
      },
      {
        "name": "Type",
        "desc": "指定key类型，默认为1，1表示默认类型，由KMS创建CMK密钥，2 表示EXTERNAL 类型，该类型需要用户导入密钥材料，参考 GetParametersForImport 和 ImportKeyMaterial 接口"
      }
    ],
    "desc": "创建用户管理数据密钥的主密钥CMK（Custom Master Key）。"
  },
  "DescribeWhiteBoxKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "白盒密钥的全局唯一标识符"
      }
    ],
    "desc": "展示白盒密钥的信息"
  },
  "GetParametersForImport": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK的唯一标识，获取密钥参数的CMK必须是EXTERNAL类型，即在CreateKey时指定Type=2 类型的CMK。"
      },
      {
        "name": "WrappingAlgorithm",
        "desc": "指定加密密钥材料的算法，目前支持RSAES_PKCS1_V1_5、RSAES_OAEP_SHA_1、RSAES_OAEP_SHA_256"
      },
      {
        "name": "WrappingKeySpec",
        "desc": "指定加密密钥材料的类型，目前只支持RSA_2048"
      }
    ],
    "desc": "获取导入主密钥（CMK）材料的参数，返回的Token作为执行ImportKeyMaterial的参数之一，返回的PublicKey用于对自主导入密钥材料进行加密。返回的Token和PublicKey 24小时后失效，失效后如需重新导入，需要再次调用该接口获取新的Token和PublicKey。"
  },
  "DisableWhiteBoxKeys": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "白盒密钥的全局唯一标识符列表。注意：要确保所有提供的KeyId是格式有效的，没有重复，个数不超过50个，并且都是有效存在的。"
      }
    ],
    "desc": "批量禁用白盒密钥"
  },
  "ListKeyDetail": {
    "params": [
      {
        "name": "Offset",
        "desc": "含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0"
      },
      {
        "name": "Limit",
        "desc": "含义跟 SQL 查询的 Limit 一致，表示本次最多获取 Limit 个元素。缺省值为10，最大值为200"
      },
      {
        "name": "Role",
        "desc": "根据创建者角色筛选，默认 0 表示用户自己创建的cmk， 1 表示授权其它云产品自动创建的cmk"
      },
      {
        "name": "OrderType",
        "desc": "根据CMK创建时间排序， 0 表示按照降序排序，1表示按照升序排序"
      },
      {
        "name": "KeyState",
        "desc": "根据CMK状态筛选， 0表示全部CMK， 1 表示仅查询Enabled CMK， 2 表示仅查询Disabled CMK，3 表示查询PendingDelete 状态的CMK(处于计划删除状态的Key)，4 表示查询 PendingImport 状态的CMK"
      },
      {
        "name": "SearchKeyAlias",
        "desc": "根据KeyId或者Alias进行模糊匹配查询"
      },
      {
        "name": "Origin",
        "desc": "根据CMK类型筛选， \"TENCENT_KMS\" 表示筛选密钥材料由KMS创建的CMK， \"EXTERNAL\" 表示筛选密钥材料需要用户导入的 EXTERNAL类型CMK，\"ALL\" 或者不设置表示两种类型都查询，大小写敏感。"
      },
      {
        "name": "KeyUsage",
        "desc": "根据CMK的KeyUsage筛选，ALL表示筛选全部，可使用的参数为：ALL 或 ENCRYPT_DECRYPT 或 ASYMMETRIC_DECRYPT_RSA_2048 或 ASYMMETRIC_DECRYPT_SM2，为空则默认筛选ENCRYPT_DECRYPT类型"
      }
    ],
    "desc": "根据指定Offset和Limit获取主密钥列表详情。"
  },
  "AsymmetricRsaDecrypt": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK的唯一标识"
      },
      {
        "name": "Ciphertext",
        "desc": "使用PublicKey加密的密文，Base64编码"
      },
      {
        "name": "Algorithm",
        "desc": "在使用公钥加密时对应的算法：当前支持RSAES_PKCS1_V1_5、RSAES_OAEP_SHA_1、RSAES_OAEP_SHA_256"
      }
    ],
    "desc": "使用指定的RSA非对称密钥的私钥进行数据解密，密文必须是使用对应公钥加密的。处于Enabled 状态的非对称密钥才能进行解密操作。"
  },
  "DisableKeyRotation": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK唯一标识符"
      }
    ],
    "desc": "对指定的CMK禁止密钥轮换功能。"
  },
  "DisableWhiteBoxKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "白盒密钥的全局唯一标识符"
      }
    ],
    "desc": "禁用白盒密钥"
  },
  "EnableKeys": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "需要批量启用的CMK Id 列表， CMK数量最大支持100"
      }
    ],
    "desc": "该接口用于批量启用CMK。"
  },
  "ScheduleKeyDeletion": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK的唯一标志"
      },
      {
        "name": "PendingWindowInDays",
        "desc": "计划删除时间区间[7,30]"
      }
    ],
    "desc": "CMK计划删除接口，用于指定CMK删除的时间，可选时间区间为[7,30]天"
  },
  "DescribeKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK全局唯一标识符"
      }
    ],
    "desc": "用于获取指定KeyId的主密钥属性详情信息。"
  },
  "EnableKeyRotation": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK唯一标识符"
      }
    ],
    "desc": "对指定的CMK开启密钥轮换功能。"
  },
  "CreateWhiteBoxKey": {
    "params": [
      {
        "name": "Alias",
        "desc": "作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字母数字 - _ 的组合，首字符必须为字母或者数字。Alias不可重复。"
      },
      {
        "name": "Algorithm",
        "desc": "创建密钥所有的算法类型，支持的取值：AES_256,SM4"
      },
      {
        "name": "Description",
        "desc": "密钥的描述，最大1024字节"
      }
    ],
    "desc": "创建白盒密钥。 密钥个数的上限为 50。"
  },
  "EnableWhiteBoxKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "白盒密钥的全局唯一标识符"
      }
    ],
    "desc": "启用白盒密钥"
  },
  "EnableKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK唯一标识符"
      }
    ],
    "desc": "用于启用一个指定的CMK。"
  },
  "Decrypt": {
    "params": [
      {
        "name": "CiphertextBlob",
        "desc": "待解密的密文数据"
      },
      {
        "name": "EncryptionContext",
        "desc": "key/value对的json字符串，如果Encrypt指定了该参数，则在调用Decrypt API时需要提供同样的参数，最大支持1024字符"
      }
    ],
    "desc": "本接口用于解密密文，得到明文数据。"
  },
  "DescribeKeys": {
    "params": [
      {
        "name": "KeyIds",
        "desc": "查询CMK的ID列表，批量查询一次最多支持100个KeyId"
      }
    ],
    "desc": "该接口用于批量获取主密钥属性信息。"
  },
  "DescribeWhiteBoxServiceStatus": {
    "params": [],
    "desc": "获取白盒密钥服务状态"
  },
  "UpdateKeyDescription": {
    "params": [
      {
        "name": "Description",
        "desc": "新的描述信息，最大支持1024字节"
      },
      {
        "name": "KeyId",
        "desc": "需要修改描述信息的CMK ID"
      }
    ],
    "desc": "该接口用于对指定的cmk修改描述信息。对于处于PendingDelete状态的CMK禁止修改。"
  },
  "GetServiceStatus": {
    "params": [],
    "desc": "用于查询该用户是否已开通KMS服务"
  },
  "DescribeWhiteBoxDecryptKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "白盒密钥的全局唯一标识符"
      }
    ],
    "desc": "获取白盒解密密钥"
  }
}