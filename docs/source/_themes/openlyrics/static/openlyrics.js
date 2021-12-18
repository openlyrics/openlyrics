document.addEventListener('DOMContentLoaded', function(event) {

  // Add data-column="" HTML5 data-* attributes for every table cell.
  let i, j = 0;
  let tables = document.querySelectorAll('table.docutils');
  tables.forEach(function(elTable, nTableIndex) {
    if (elTable.tHead.rows.length > 0 ) {
      for (i = 0; i < elTable.tHead.rows[0].cells.length; i++) {
        for (j = 1; j < elTable.rows.length; j++) {
          elTable.rows[j].cells[i].dataset.column = elTable.tHead.rows[0].cells[i].textContent;
        }
      }
    };
  })
});

