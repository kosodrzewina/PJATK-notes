# RBD

## 000 true, false, null

### AND

| and   | true  | false | null |
| ----- | ----- | ----- | ---- |
| true  | true  | false | null |
| false | false | false | null |
| null  | null  | null  | null |

### OR

| or    | true | false | null |
| ----- | ---- | ----- | ---- |
| true  | true | true  | null |
| false | true | false | null |
| null  | null | null  | null |

### NULL

| and   | true  | false | null |
| ----- | ----- | ----- | ---- |
| true  | false | true  | null |
| false | true  | false | null |
| null  | null  | null  | null |
