# Python-LinkedList
Linkedlist data structure to work with python.
<br>

### Installation
```python
pip install pylinkedlist
```
<br>

### Uninstallation
```python
pip uninstall pylinkedlist
```
<br>

### Importing Package
```python
import pylinkedlist as llist
```
<br>

### Initializing A LinkedList
Initialize a variable var with Linkedlist data structure.
```python
var = llist.LinkedList()
```
<br>

### Adding Element in the LinkedList
#### Appending at the end
Add element[s] at the end of linkedlist
```python
# x can be a list or single elememnt
var.add(x)
```
#### Adding in the front
Add element[s] at the front of linkedlist
```python
# x can be a list or single elememnt
var.addleft(x)
```
<br>

### Count of Nodes in the LinkedList
```python
count = var.getcount()
```
<br>

### Reference of Node in the LinkedList
```python
count = var.getnode()
```
<br>

### Find Middle Element in the LinkedList
```python
count = var.getmid()
```
<br>

### Delete A Node From LinkedList
```python
count = var.delete_from_mid(x)
```
<br>

### Remove Duplicates from the LinkedList
Pass the argument **isSorted = True** or **isSorted = False** if it is sorted or not.
```python
count = var.removeDuplictaes(isSorted = True)
or
count = var.removeDuplicates(isSorted = False)
```
<br>

### Insert At Mid
```python
var.insert_at_mid(x)
```
<br>

### Element at Given Position
```python
element = var.at(x)
```