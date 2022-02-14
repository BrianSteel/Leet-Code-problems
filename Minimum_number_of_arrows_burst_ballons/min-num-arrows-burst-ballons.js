/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    // if length 0 or 1 return 0 or 1 respectively
    let length = points.length;
    if(length === 0) return 0;
    if(length === 1) return 1;

    // Numerical sorting of the points according to end position of balloon
    // sorting based on the first value wont work see python example
    points.sort((a,b) => {
        return a[1]-b[1]; 
    })

    // store the second position of the first
    let arrow = points[0][1]
    // because zero is already handled so it must be atleast more than 1
    shots = 1;
    // loop through the points, you can leave the first because you already considered that in arrow and shots
    // you now first have to arrow value to point[1][1], then point[2][1] and so on
    for(let i = 1; i<length; i++){
        // if saved value is greater than lets say point[1][1] no need to increase shots needed as one shot can take out both
        if(arrow >= points[i][0]){
            continue;
        }
        // else increase the shots and update saved arrow to the next point let say next will arrow = point[1][1]
        shots++;
        arrow = points[i][1];
    }
    return shots;
};

console.log(findMinArrowShots([[1,4], [3,7], [4,6]]))