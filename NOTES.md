Regex to refactor to new external pin method:

```
(\w*)\.val = ([1|0])
$1.setExternalPin($2)
```
