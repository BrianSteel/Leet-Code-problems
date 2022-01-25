/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */

const searchMatrix = function(matrix, target) {
    if(matrix.length === 0){
        return false;
    }
    let solo_arr = [];
    for (let i=0; i<matrix.length; i++){
        let start = matrix[i][0];
        let end = matrix[i][matrix[i].length-1];
        if(start<=target && end>=target){
            solo_arr = matrix[i]
            break;
        } 
        else if(start>target){
            return false;
        }
    }
    for(let i=0; i<solo_arr.length; i++){
        if(solo_arr[i]===target){
            return true;
        }
    }
    return false;
};