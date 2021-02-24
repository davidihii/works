function initFilter() {
  // 1- Définitions des constantes
  const items = document.querySelectorAll(".itemAgenda"),
    selectItems = document.querySelectorAll("select"),
    selectTopic = document.getElementById("selectThemes"),
    selectMonth = document.getElementById("selectMois"),
    selectFormat = document.getElementById("selectFormat"),
    selectLocation = document.getElementById("selectLocalisations");

  // 2- Initialisation des variables

  // 2-1 Variables des futures filtres en tableaux
  let optionsTopic = [],
    optionsMonth = [],
    optionsLocation = [],
    optionsFormat = [];

  // 2-2 Variables des futures exeptions
  locationValues = "";
  dateValues = "";
  locationValueArray = [""];
  dateValueArray = [""];

  // 3- Fonction permettant de transferet les valeurs 
  // de la constante items dans les tableaux du 2-1
  function constructor() {
    let optionsTopicUnclean = [],
      optionsMonthUnclean = [],
      optionsLocationUnclean = [],
      optionsFormatUnclean = [];

    // 3-1 Trie des valeurs contenues dans la constante items
    for (var item1 of items) {
      optionsTopicUnclean.push(item1.dataset.themes);
      optionsMonthUnclean.push(item1.dataset.mois);
      optionsLocationUnclean.push(item1.dataset.localisations);
      optionsFormatUnclean.push(item1.dataset.format);
    }

    // 3-2 Création de la Fonction permettant la suppression des doublons
    function removeDuplicates(arr) {
      let unique_array = [];

      for (var arr_1 of arr) {
        if (unique_array.indexOf(arr_1) == -1 && this != "blank") {
          unique_array.push(arr_1);
        }
      }
      return unique_array;
    }

    // 3-3 Suppressions des doublons puis Définition des variables initialisées en 2
    optionsTopic = removeDuplicates(optionsTopicUnclean.filter(Boolean));
    optionsMonth = removeDuplicates(optionsMonthUnclean.filter(Boolean));
    optionsLocation = removeDuplicates(optionsLocationUnclean.filter(Boolean));
    optionsFormat = removeDuplicates(optionsFormatUnclean.filter(Boolean));

    // 3_4 Récupération des valeurs dans les tableaux initialisés en 2
    locationValueArray.push(optionsLocation);
    dateValueArray.push(optionsMonth);

    // 3-5 Fonction qui permet de pousser les différentes options 
    // dans le selecteur correspondant
    function addOption(select, options) {
      for (var option of options) {
        let element = document.createElement("option");
        element.text = option;
        select.add(element);
      }
    }

    addOption(selectTopic, optionsTopic);
    addOption(selectMonth, optionsMonth);
    addOption(selectLocation, optionsLocation);
    addOption(selectFormat, optionsFormat);
  }

  // 4- Création de la Fonction qui permettra de gérer les exeptions
  function filterExceptions() {
    // 4-1 Définition de la variable permettant de gérer les exeptions
    let catchItemsFormat = document.querySelectorAll(".itemAgenda");

    // 4-2 Récupération des valeurs des tableaux dans des variables string
    locationValues = locationValueArray.toString();
    dateValues = dateValueArray.toString();

    // 4_3 Boucle créant les exeptions
    for (var catchItemFormat of catchItemsFormat) {
      catchItemFormat.getAttribute("data-format") == "distanciel"
        ? catchItemFormat.setAttribute("data-localisations", locationValues)
        : 0;

      catchItemFormat.getAttribute("data-format") == "téléchargeable"
        ? catchItemFormat.setAttribute("data-localisations", locationValues)
        : 0;

      catchItemFormat.getAttribute("data-format") == "téléchargeable"
        ? catchItemFormat.setAttribute("data-mois", dateValues)
        : 0;
    }
  }
  // 5- Fonction qui filtre les formations
  function filterSelect(select, itemTopic, itemDate, itemFormat, itemLocation) {
    // 5-1 Création des variables permettant de comparer filtres et attribus
    let selectedOptions = [""],
      itemsAttributes = [""];

    // 5-2 Récupération des valeurs contenues dans les selecteurs
    for (var _this of select) {
      selectedOptions.push(_this.value);
    }
    // 5-3 Boucle permettant de filtrer les formations
    for (var item of items) {
      // 5-3-1 Récupération des valeurs contenues dans les attribus des items
      itemsAttributes.push(item.getAttribute(itemTopic));
      itemsAttributes.push(item.getAttribute(itemDate));
      itemsAttributes.push(item.getAttribute(itemFormat));
      itemsAttributes.push(item.getAttribute(itemLocation));

      // 5-3-2 Création de la variable show qui stock un int
      let show = selectItems.length * 4;

      // 5-4-3 Boucle qui filtre les items
      for (var item_Attribute of itemsAttributes) {
        for (var selected_Option of selectedOptions) {
          // 5-4-3-1 Variable temporaire qui stock la valeur 
          // en sortie de l'opérateur ternaire
          temp_Item_Attribute =
            selected_Option != ""
              ? item_Attribute.search(selected_Option) > -1
                ? selected_Option
                : item_Attribute
              : item_Attribute;

          // 5-4-3-2 La variable show s'incrémente d'une valeur retourné
          // après comparaison la valeur temp avec la valeur du filtre
          show += temp_Item_Attribute == selected_Option ? 1 : -1;

          // 5-4-3-3 Cache ou non la formation 
          item.classList.toggle("hide", show = 0);
        }
      }
    }
  }

  constructor();
  filterExceptions();
  filterSelect(
    selectItems,
    "data-themes",
    "data-mois",
    "data-format",
    "data-localisations"
  );

  // 6- Au changement d'un filtre recharge les éléments 
  for (var selectItem of selectItems) {
    selectItem.onchange = function () {
      filterSelect(
        selectItems,
        "data-themes",
        "data-mois",
        "data-format",
        "data-localisations"
      );
    };
  }
}
window.onload = initFilter;
