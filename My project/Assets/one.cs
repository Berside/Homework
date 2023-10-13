using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class one : MonoBehaviour
{
    public GameObject b;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void On()
    {
        if (b.active)
            b.SetActive(false);
        else
            b.SetActive(true);
    }
}
