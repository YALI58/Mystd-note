---
media: https://www.bilibili.com/video/BV1ps4y1d73V?p=43
---

- ![[3.5.4_Cache替换算法PT1M51.423S.webp|3.5.4_Cache替换算法 - 01:51|50]] [01:51](https://www.bilibili.com/video/BV1ps4y1d73V?p=43&t=111.423175#t=01:51.42) 替换算法 在三个映射。
- ![[3.5.4_Cache替换算法PT7M13.636S.webp|3.5.4_Cache替换算法 - 07:13|50]] [07:13](https://www.bilibili.com/video/BV1ps4y1d73V?p=43&t=433.635789#t=07:13.64) 先进先出算法 抖动现象，频繁的换入换出现象（刚被替换很快又被调入）
- ![[3.5.4_Cache替换算法PT19M9.852S.webp|3.5.4_Cache替换算法 - 19:09|50]] [19:09](https://www.bilibili.com/video/BV1ps4y1d73V?p=43&t=1149.851621#t=19:09.85) 近期最少使用算法（LRU）采用全相连映射，Cache块的总数=2^n,计数器位数就为n，且Cache装满后所有计数器的值一定不重复。计数器最大数字不会大于2^n -1。
- ![[3.5.4_Cache替换算法PT20M23.925S.webp|3.5.4_Cache替换算法 - 20:23|50]] [20:23](https://www.bilibili.com/video/BV1ps4y1d73V?p=43&t=1223.924781#t=20:23.92) 若是被频繁的主存块数量>Cache行数量，则有可能发生 抖动现象
- ![[3.5.4_Cache替换算法PT24M4.134S.webp|3.5.4_Cache替换算法 - 24:04|50]] [24:04](https://www.bilibili.com/video/BV1ps4y1d73V?p=43&t=1444.133882#t=24:04.13)   当命中了，计数器才加1.当贝替代，计数器置为0