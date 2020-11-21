# EPAi session13 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session13 objectives
This assignment, helps to code the concepts that are learnt in the session 13 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

- Sequence Types - Part I

---

Look at the test_polygons_modules.ipynb jupyter notebook to run some sameple test cases and examples.
 
---
## Polygon
class methods


**__init__(self, num_edges, circum_radius)**

        Instantiate a Polygon
         : param num_edges : 
         : param circum_radius : 

**__repr__(self)**

        Representation of a polygon
         : return :  str

**__eq__(self, other)**

        Check for equality of two polygons
         : param other :  Other Polygon
         : return :  bool

**__gt__(self, other)**

        Verify if the current polygon is greater than the other polygon
         : param other :  another polygon
         : return :  bool

---
## PolygonsSequence
class methods

**__init__(self, max_verties, circum_radius)**

        Initialize the polynomial sequence
         : param max_verties :  int
         : param circum_radius :  float

**max_efficiency_polygon(self)**

        determine the polynomial with maximum efficiency
         : return :  Polynomial

**__getitem__(self, item)**

        Implementing getitem to make this Class a sequence
         : param item :  index for the sequence
         : return :  the polynomial element

**__len__(self)**

        Determine the length of the sequence
         : return :  int

**__repr__(self)**

        Formatted representation of the poly sequence
         : return :  str
