var escalaCores = { 
    sequencial: { 
        verde: [ 
        ["#E5F5E0","#A1D99B","#31A354"], 
        ["#EDF8E9","#BAE4B3","#74C476","#238B45"], 
        ["#EDF8E9","#BAE4B3","#74C476","#31A354","#006D2C"], 
        ["#EDF8E9","#C7E9C0","#A1D99B","#74C476","#31A354","#006D2C"], 
        ["#EDF8E9","#C7E9C0","#A1D99B","#74C476","#41AB5D","#238B45","#005A32"], 
        ["#F7FCF5","#E5F5E0","#C7E9C0","#A1D99B","#74C476","#41AB5D","#238B45","#005A32"]
        ], 
        azul: [ 
        ["#DEEBF7","#9ECAE1","#3182BD"], 
        ["#EFF3FF","#BDD7E7","#6BAED6","#2171B5"], 
        ["#EFF3FF","#BDD7E7","#6BAED6","#3182BD","#08519C"], 
        ["#EFF3FF","#C6DBEF","#9ECAE1","#6BAED6","#3182BD","#08519C"], 
        ["#EFF3FF","#C6DBEF","#9ECAE1","#6BAED6","#4292C6","#2171B5","#084594"], 
        ["#F7FBFF","#DEEBF7","#C6DBEF","#9ECAE1","#6BAED6","#4292C6","#2171B5","#084594"]
        ], 
        laranja: [ 
        ["#FEE6CE","#FDAE6B","#E6550D"], 
        ["#FEEDDE","#FDBE85","#FD8D3C","#D94701"], 
        ["#FEEDDE","#FDBE85","#FD8D3C","#E6550D","#A63603"], 
        ["#FEEDDE","#FDD0A2","#FDAE6B","#FD8D3C","#E6550D","#A63603"], 
        ["#FEEDDE","#FDD0A2","#FDAE6B","#FD8D3C","#F16913","#D94801","#8C2D04"], 
        ["#FFF5EB","#FEE6CE","#FDD0A2","#FDAE6B","#FD8D3C","#F16913","#D94801","#8C2D04"]
        ], 
        amarelo: [ 
        ["#F7FCB9","#ADDD8E","#31A354"], 
        ["#FFFFCC","#C2E699","#78C679","#238443"], 
        ["#FFFFCC","#C2E699","#78C679","#31A354","#006837"], 
        ["#FFFFCC","#D9F0A3","#ADDD8E","#78C679","#31A354","#006837"], 
        ["#FFFFCC","#D9F0A3","#ADDD8E","#78C679","#41AB5D","#238443","#005A32"], 
        ["#FFFFE5","#F7FCB9","#D9F0A3","#ADDD8E","#78C679","#41AB5D","#238443","#005A32"]
        ], 
        vermelho: [ 
        ["#FEE0D2","#FC9272","#DE2D26"], 
        ["#FEE5D9","#FCAE91","#FB6A4A","#CB181D"], 
        ["#FEE5D9","#FCAE91","#FB6A4A","#DE2D26","#A50F15"], 
        ["#FEE5D9","#FCBBA1","#FC9272","#FB6A4A","#DE2D26","#A50F15"], 
        ["#FEE5D9","#FCBBA1","#FC9272","#FB6A4A","#EF3B2C","#CB181D","#99000D"], 
        ["#FFF5F0","#FEE0D2","#FCBBA1","#FC9272","#FB6A4A","#EF3B2C","#CB181D","#99000D"]
        ]
    }, 
    qualitativa: { 
        verde: [ 
        ["#B3E2CD","#FDCDAC","#CBD5E8"], 
        ["#B3E2CD","#FDCDAC","#CBD5E8","#F4CAE4"], 
        ["#B3E2CD","#FDCDAC","#CBD5E8","#F4CAE4","#E6F5C9;"], 
        ["#B3E2CD","#FDCDAC","#CBD5E8","#F4CAE4","#E6F5C9","#FFF2AE"], 
        ["#B3E2CD","#FDCDAC","#CBD5E8","#F4CAE4","#E6F5C9","#FFF2AE","#F1E2CC"], 
        ["#B3E2CD","#FDCDAC","#CBD5E8","#F4CAE4","#E6F5C9","#FFF2AE","#F1E2CC","#CCCCCC"]
        ], 
        azul: [ 
        ["#A6CEE3","#1F78B4","#B2DF8A"], 
        ["#A6CEE3","#1F78B4","#B2DF8A","#33A02C"], 
        ["#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99"], 
        ["#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C"], 
        ["#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F"], 
        ["#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00"]
        ], 
        laranja: [ 
        ["#66C2A5","#FC8D62","#8DA0CB"], 
        ["#66C2A5","#FC8D62","#8DA0CB","#E78AC3"], 
        ["#66C2A5","#FC8D62","#8DA0CB","#E78AC3","#A6D854"], 
        ["#66C2A5","#FC8D62","#8DA0CB","#E78AC3","#A6D854","#FFD92F"], 
        ["#66C2A5","#FC8D62","#8DA0CB","#E78AC3","#A6D854","#FFD92F","#E5C494"], 
        ["#66C2A5","#FC8D62","#8DA0CB","#E78AC3","#A6D854","#FFD92F","#E5C494","#B3B3B3"]
        ], 
        amarelo: [ 
        ["#8DD3C7","#FFFFB3","#BEBADA"], 
        ["#8DD3C7","#FFFFB3","#BEBADA","#FB8072"], 
        ["#8DD3C7","#FFFFB3","#BEBADA","#FB8072","#80B1D3"], 
        ["#8DD3C7","#FFFFB3","#BEBADA","#FB8072","#80B1D3","#FDB462"], 
        ["#8DD3C7","#FFFFB3","#BEBADA","#FB8072","#80B1D3","#FDB462","#B3DE69"], 
        ["#8DD3C7","#FFFFB3","#BEBADA","#FB8072","#80B1D3","#FDB462","#B3DE69","#FCCDE5"]
        ], 
        vermelho: [ 
        ["#FBB4AE","#B3CDE3","#CCEBC5"], 
        ["#FBB4AE","#B3CDE3","#CCEBC5","#DECBE4"], 
        ["#FBB4AE","#B3CDE3","#CCEBC5","#DECBE4","#FED9A6"], 
        ["#FBB4AE","#B3CDE3","#CCEBC5","#DECBE4","#FED9A6","#FFFFCC"], 
        ["#FBB4AE","#B3CDE3","#CCEBC5","#DECBE4","#FED9A6","#FFFFCC","#E5D8BD"], 
        ["#FBB4AE","#B3CDE3","#CCEBC5","#DECBE4","#FED9A6","#FFFFCC","#E5D8BD","#FDDAEC"]
        ]
    }, 
    divergente: { 
        verde: [ 
        ["#FC8D59","#FFFFBF","#91CF60"], 
        ["#D7191C","#FDAE61","#A6D96A","#1A9641"], 
        ["#D7191C","#FDAE61","#FFFFBF","#A6D96A","#1A9641"], 
        ["#D73027","#FC8D59","#FEE08B","#D9EF8B","#91CF60","#1A9850"], 
        ["#D73027","#FC8D59","#FEE08B","#FFFFBF","#D9EF8B","#91CF60","#1A9850"], 
        ["#D73027","#F46D43","#FDAE61","#FEE08B","#D9EF8B","#A6D96A","#66BD63","#1A9850"]
        ], 
        azul: [ 
        ["#FC8D59","#FFFFBF","#91BFDB"], 
        ["#D7191C","#FDAE61","#ABD9E9","#2C7BB6"], 
        ["#D7191C","#FDAE61","#FFFFBF","#ABD9E9","#2C7BB6"], 
        ["#D73027","#FC8D59","#FEE090","#E0F3F8","#91BFDB","#4575B4"], 
        ["#D73027","#FC8D59","#FEE090","#FFFFBF","#E0F3F8","#91BFDB","#4575B4"], 
        ["#D73027","#F46D43","#FDAE61","#FEE090","#E0F3F8","#ABD9E9","#74ADD1","#4575B4"]
        ], 
        laranja: [ 
        ["#D8B365","#F5F5F5","#5AB4AC"], 
        ["#A6611A","#DFC27D","#80CDC1","#018571"], 
        ["#A6611A","#DFC27D","#F5F5F5","#80CDC1","#018571"], 
        ["#8C510A","#D8B365","#F6E8C3","#C7EAE5","#5AB4AC","#01665E"], 
        ["#8C510A","#D8B365","#F6E8C3","#F5F5F5","#C7EAE5","#5AB4AC","#01665E"], 
        ["#8C510A","#BF812D","#DFC27D","#F6E8C3","#C7EAE5","#80CDC1","#35978F","#01665E"]
        ], 
        amarelo: [ 
        ["#FC8D59","#FFFFBF","#99D594"], 
        ["#D7191C","#FDAE61","#ABDDA4","#2B83BA"], 
        ["#D7191C","#FDAE61","#FFFFBF","#ABDDA4","#2B83BA"], 
        ["#D53E4F","#FC8D59","#FEE08B","#E6F598","#99D594","#3288BD"], 
        ["#D53E4F","#FC8D59","#FEE08B","#FFFFBF","#E6F598","#99D594","#3288BD"], 
        ["#D53E4F","#F46D43","#FDAE61","#FEE08B","#E6F598","#ABDDA4","#66C2A5","#3288BD"]
        ], 
        vermelho: [ 
        ["#EF8A62","#F7F7F7","#67A9CF"], 
        ["#CA0020","#F4A582","#92C5DE","#0571B0"], 
        ["#CA0020","#F4A582","#F7F7F7","#92C5DE","#0571B0"], 
        ["#B2182B","#EF8A62","#FDDBC7","#D1E5F0","#67A9CF","#2166AC"], 
        ["#B2182B","#EF8A62","#FDDBC7","#F7F7F7","#D1E5F0","#67A9CF","#2166AC"], 
        ["#B2182B","#D6604D","#F4A582","#FDDBC7","#D1E5F0","#92C5DE","#4393C3","#2166AC"]
        ]
    }
};

var LegendaCor = function(tipoEscala, corEscala, min, max, qtdCores, titulo, unidade, casasDecimais){
    this.escala = escalaCores[tipoEscala][corEscala][qtdCores-3];
    this.titulo = titulo;
    this.unidade = unidade;

    var i=0;
    t = (Math.round(parseFloat(((max-min)/(qtdCores)) * Math.pow(10, casasDecimais)) / Math.pow(10, casasDecimais)));

    this.tabela = new Object();

    k = 0;

    mn=min;
    for(i=0;i<qtdCores;i++){
        mx = mn+t;
        this.tabela[i] = {
            min : mn, 
            max: mx, 
            color: this.escala[i]
            };
        mn = mx;
    }
    this.tabela[qtdCores-1].max = max;
};

LegendaCor.prototype.escala = function() {
    return this.escala;
};

LegendaCor.prototype.getColorByValue = function(value){
    tabela = this.tabela;
    var i=0;
	
    if(value>tabela[Object.keys(tabela).length-1].min){
        return tabela[Object.keys(tabela).length-1].color;
    }else if(value<tabela[0].min || value<tabela[0].max){
        return tabela[0].color;
    }else{
        for(i=1;i<Object.keys(tabela).length-1;i++){
            if(value>=tabela[i].min && value<tabela[i].max)
                return tabela[i].color;
        }
    }
};

LegendaCor.prototype.printColorScale = function(){
    var htmlTable = document.createElement("table");
    htmlTable.setAttribute("id", "tabela");
    htmlTable.setAttribute("style", "margin: 0px; font-weight: bold;");
    htmlTable.setAttribute("width", "100%");
    //htmlTable.setAttribute("height", "100%");
    htmlTable.setAttribute("cellspacing", "3");
	
    htmlTable.innerHTML = "<tr><td colspan='2' style='text-align: center; padding-bottom: 15px;'>"+this.titulo+"</td></tr>";
    var i=0;
    for(i=0;i<Object.keys(this.tabela).length;i++){
        htmlTable.innerHTML+="<tr><td width='12%' bgcolor='"+this.tabela[i].color+"' style='padding-bottom: 5px;'></td><td style='padding-left: 10px;'>De "+parseFloat(this.tabela[i].min.toFixed(2))+" a "+parseFloat(this.tabela[i].max.toFixed(2))+"</td></tr>";
    }
	
    return htmlTable;
};
