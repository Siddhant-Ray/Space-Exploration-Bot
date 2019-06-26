using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using System.Threading;
using UnityEditor;

public class questions : MonoBehaviour
{
    public TextAsset file;
    public Text Valuetexttemp;
    public Text Valuetexthum;
    public Text Valuetextuv;
    public Text Valuetextco;
    public Text Valuetexthh;
    public Text Valuetextcoo;


    void Start()
    {
        Load(file);
        for (int i = 1; i <= 10; i++)
        {

            Valuetexttemp.text = Find_id(i.ToString()).temp + "C";
            Valuetexthum.text = Find_id(i.ToString()).humid + "%";
            Valuetextuv.text = Find_id(i.ToString()).uv + "%";
            Valuetextco.text = Find_id(i.ToString()).co + "%";
            Valuetextcoo.text = Find_id(i.ToString()).co2 + "%";
            Valuetexthh.text = Find_id(i.ToString()).h2 + "%";
            Debug.Log(Find_id(i.ToString()).temp);
        }
    }
    public class Row
    {
        public string id;
        public string temp;
        public string humid;
        public string uv;
        public string co;
        public string co2;
        public string h2;

    }

    List<Row> rowList = new List<Row>();
    bool isLoaded = false;

    public bool IsLoaded()
    {
        return isLoaded;
    }

    public List<Row> GetRowList()
    {
        return rowList;
    }

    public void Load(TextAsset csv)
    {
        rowList.Clear();
        string[][] grid = CsvParser2.Parse(csv.text);
        for (int i = 1; i < grid.Length; i++)
        {
            Row row = new Row();
            row.id = grid[i][0];
            row.temp = grid[i][1];
            row.humid = grid[i][2];
            row.uv = grid[i][3];
            row.co = grid[i][4];
            row.co2 = grid[i][5];
            row.h2 = grid[i][6];

            rowList.Add(row);
        }
        isLoaded = true;
    }

    public int NumRows()
    {
        return rowList.Count;
    }

    public Row GetAt(int i)
    {
        if (rowList.Count <= i)
            return null;
        return rowList[i];
    }

    public Row Find_id(string find)
    {
        return rowList.Find(x => x.id == find);
    }
    public List<Row> FindAll_id(string find)
    {
        return rowList.FindAll(x => x.id == find);
    }
    public Row Find_temp(string find)
    {
        return rowList.Find(x => x.temp == find);
    }
    public List<Row> FindAll_temp(string find)
    {
        return rowList.FindAll(x => x.temp == find);
    }
    public Row Find_humid(string find)
    {
        return rowList.Find(x => x.humid == find);
    }
    public List<Row> FindAll_humid(string find)
    {
        return rowList.FindAll(x => x.humid == find);
    }
    public Row Find_uv(string find)
    {
        return rowList.Find(x => x.uv == find);
    }
    public List<Row> FindAll_uv(string find)
    {
        return rowList.FindAll(x => x.uv == find);
    }
    public Row Find_co(string find)
    {
        return rowList.Find(x => x.co == find);
    }
    public List<Row> FindAll_co(string find)
    {
        return rowList.FindAll(x => x.co == find);
    }
    public Row Find_co2(string find)
    {
        return rowList.Find(x => x.co2 == find);
    }
    public List<Row> FindAll_co2(string find)
    {
        return rowList.FindAll(x => x.co2 == find);
    }
    public Row Find_h2(string find)
    {
        return rowList.Find(x => x.h2 == find);
    }
    public List<Row> FindAll_h2(string find)
    {
        return rowList.FindAll(x => x.h2 == find);
    }

}