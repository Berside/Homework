using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class bd : MonoBehaviour
{
    public GameObject sq;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void wb()
    {
        if (sq.activeInHierarchy == true)
            sq.SetActive(false);
        else
            sq.SetActive(true);
    }
}
