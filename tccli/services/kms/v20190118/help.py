# -*- coding: utf-8 -*-
DESC = "kms-2019-01-18"
INFO = {
  "GetKeyRotationStatus": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK唯一标识符"
      }
    ],
    "desc": "查询指定的CMK是否开启了密钥轮换功能。"
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
  "EnableKeyRotation": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK唯一标识符"
      }
    ],
    "desc": "对指定的CMK开启密钥轮换功能。"
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
  "CreateKey": {
    "params": [
      {
        "name": "Alias",
        "desc": "作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字符或数字的组合"
      },
      {
        "name": "Description",
        "desc": "CMK 的描述，最大1024字节"
      },
      {
        "name": "KeyUsage",
        "desc": "指定key的用途。目前，仅支持\"ENCRYPT_DECRYPT\"，默认为  \"ENCRYPT_DECRYPT\"，即key用于加密和解密"
      },
      {
        "name": "Type",
        "desc": "指定key类型，1为当前地域默认类型，默认为1，且当前只支持该类型"
      }
    ],
    "desc": "创建用户管理数据密钥的主密钥CMK（Custom Master Key）。"
  },
  "UpdateAlias": {
    "params": [
      {
        "name": "Alias",
        "desc": "新的别名，1-64个字符或数字的组合"
      },
      {
        "name": "KeyId",
        "desc": "CMK的全局唯一标识符"
      }
    ],
    "desc": "用于修改CMK的别名。"
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
        "desc": "被加密的密文数据"
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
  "UpdateKeyDescription": {
    "params": [
      {
        "name": "Description",
        "desc": "新的描述信息，最大支持1024字节"
      },
      {
        "name": "KeyId",
        "desc": "需要修改描述信息的的CMK ID"
      }
    ],
    "desc": "该接口用于对指定的cmk修改描述信息。"
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
  "DisableKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK唯一标识符"
      }
    ],
    "desc": "本接口用于禁用一个主密钥，处于禁用状态的Key无法用于加密、解密操作。"
  },
  "GetServiceStatus": {
    "params": [],
    "desc": "用于查询该用户是否已开通KMS服务"
  },
  "GenerateDataKey": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK全局唯一标识符"
      },
      {
        "name": "KeySpec",
        "desc": "指定生成Datakey的加密算法以及Datakey大小，AES_128或者AES_256。默认为AES_256"
      },
      {
        "name": "NumberOfBytes",
        "desc": "生成的DataKey的长度，同时指定NumberOfBytes和KeySpec时，以NumberOfBytes为准。最小值为1， 最大值为1024"
      },
      {
        "name": "EncryptionContext",
        "desc": "key/value对的json字符串，如果使用该字段，则返回的DataKey在解密时需要填入相同的字符串"
      }
    ],
    "desc": "本接口生成一个数据密钥，您可以用这个密钥进行本地数据的加密。"
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
    "desc": "列出账号下面的密钥列表（KeyId信息）。"
  },
  "ListKeyDetail": {
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
      },
      {
        "name": "OrderType",
        "desc": "根据CMK创建时间排序， 0 表示按照降序排序，1表示按照升序排序"
      },
      {
        "name": "KeyState",
        "desc": "根据CMK状态筛选， 0表示全部CMK， 1 表示仅查询Enabled CMK， 2 表示仅查询Disabled CMK"
      },
      {
        "name": "SearchKeyAlias",
        "desc": "根据KeyId或者Alias进行模糊匹配查询"
      }
    ],
    "desc": "根据指定Offset和Limit获取主密钥列表详情。"
  },
  "DisableKeyRotation": {
    "params": [
      {
        "name": "KeyId",
        "desc": "CMK唯一标识符"
      }
    ],
    "desc": "对指定的CMK禁止密钥轮换功能。"
  }
}