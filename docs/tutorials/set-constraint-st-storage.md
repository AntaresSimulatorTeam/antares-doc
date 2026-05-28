# Additional constraints on storages

!!! info 
    This feature was added in Antares v9.2.

In Antares, you can set additional constraints on short-term storages. 
There 3 variables you can constraint: the variation of level, the charge 
(or incoming power) and the discharge (or outgoing power).

!!! tip
    Refer to the 
    [model of the additional constraints](../reference/storages.md#additional-constraint-model){:target="_blank"}
    for a deeper understanding.

To do that first go to the **Modeling** > **Areas** > **Storages** > **Additional** 
constraints tab.

## Initialize the constraint

Give your constraint a name and select the variable on which you want to make
the constraint and the bound.

## Set the occurences

As additional constraints are coupling different time-steps together throughout 
the 168h week. So you have to edit the occurences 

First, you have to select the number of occurences.
It will create $n$ distinct columns for your occurences.

Then, you can select manually the occurences by checking the boxes. 
Or you can use the **Hours** field to input a range of hours or a particular one.
Moreover, you can set an offset for example to set a constraint on different days.

!!! example
    Let's say you want to set a constraint on each day of the week between 10am and 2pm.
    First create 7 occurences of your constraint. Then input the range `10-14` and the offset
    `24`. Click on **Enable** and you're done!

Finally, when you apply your changes, a summary of your occurences will be
displayed in the **Additional constraints** tab. 

## Set the right hand side

The right hand side of the constraint is a time series. 
Similarly to the binding constraints, you can add a time series.
You can check how you right hand side time series is taken into account in the 
[model](../reference/storages.md#additional-constraint-model) of the additional constraints.



