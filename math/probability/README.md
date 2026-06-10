poisson.py
exponential.py
normal.py
```mermaid
flowchart TD
    A["__init__ called"] --> B{data is not None?}
    B -->|Yes| C["self.data = data<br/>triggers data.setter"]
    B -->|No| D["self.mean = mean<br/>self.stdev = stdev"]
    
    C --> E["Validate: is list?"]
    E --> F["Validate: len >= 2?"]
    F --> G["Validate: all numbers?"]
    G --> H["self.__data = value"]
    
    H --> I["Calculate mean<br/>self.__mean = __calculate_mean value"]
    I --> J["Calculate stdev<br/>self.__stdev = __calculate_stdev value"]
    
    J --> K["__calculate_mean execution"]
    K --> L["return sum/len"]
    L --> M["Back to stdev calc"]
    
    M --> N["__calculate_stdev execution"]
    N --> O["Loop: for each data point"]
    O --> P["Get mean value"]
    P --> Q["dev = mean - data[i]"]
    Q --> R["Square it: dev²"]
    R --> S["Append to list"]
    S --> T{More values?}
    T -->|Yes| O
    T -->|No| U["Sum all squared devs"]
    U --> V["Divide by N-1<br/>(sample stdev)"]
    V --> W["Take square root"]
    W --> X["return result"]
```
