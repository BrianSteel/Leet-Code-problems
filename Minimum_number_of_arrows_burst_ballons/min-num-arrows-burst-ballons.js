/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    let length = points.length;
    if(length === 0) return 0;
    if(length === 1) return 1;
    points.sort((a,b) => {
        return a[1]-b[1];
    })
    let arrow = points[0][1]
    shots = 1;
    for(let i = 0; i<length; i++){
        if(arrow >= points[i][0]){
            continue;
        }
        shots++;
        arrow = points[i][1];
    }
    return shots;
};