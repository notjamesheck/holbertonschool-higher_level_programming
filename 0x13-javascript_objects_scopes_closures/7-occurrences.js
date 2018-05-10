#!/usr/bin/node
// number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  return list.filter(function (val) {
    return val === searchElement;
  }).length;
};
