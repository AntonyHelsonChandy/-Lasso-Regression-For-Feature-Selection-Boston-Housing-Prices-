# -Lasso-Regression-For-Feature-Selection-Boston-Housing-Prices-
<h3>Objective:</h3>
In this analysis we try to use lasso regression to discover the most suitable explanatory attributes that influence the prices of housing. Of these, medv is the response variable while the other 13 variables are possible predictors. At the end of the analysis, we will arrange the top five attributes based on the strength of its influence on the response (medv).
<h3>Lasso Regression:</h3>
Using the lasso regression, we can obtain the important features of the dataset, that minimizes prediction error for a quantitative response variable. The lasso does this by imposing a constraint on the model parameters that cause regression coefficients for some variables to shrink toward zero.
<h3>Boston Dataset:</h3>
The sklearn Boston dataset is used wisely in regression and is famous dataset from the 1970’s. There are 506 instances and 14 attributes in the dataset.
<h3>Conclusion</h3>
House prices also tend to be higher closer to the Charles River, and houses with more rooms are pricier. 
<img srch="output.png">
 <table style="width:100%">
  <tr>
    <th>Priority</th>
    <th>Attributes</th>

  </tr>
  <tr>
    <td>1</td>
    <td>RM: average number of rooms per dwelling</td>
  
  </tr>
   <tr>
    <td>2</td>
    <td> CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)</td>
  </tr>
   <tr>
    <td>3</td>
    <td> ZN: proportion of residential land zoned for lots over 25,000 sq.ft.</td>
  </tr>
  
   <tr>
    <td>4</td>
    <td> NOX: nitric oxides concentration (parts per 10 million)</td>
    </tr>
     <tr>
    <td>5</td>
    <td> CRIM: per capita crime rate by town</td>
  </tr>
</table> 
