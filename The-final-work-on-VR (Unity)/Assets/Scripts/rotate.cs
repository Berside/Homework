using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class rotate : MonoBehaviour
{
    public float deg = 2f;
    private GameObject go;
    private Vector3 cenLocal;
    private Rigidbody rb;

    void Start()
    {
        go = this.gameObject;

        rb = go.GetComponent<Rigidbody>();
        cenLocal = go.GetComponent<BoxCollider>().center; // Center (local space)
    }


    private void FixedUpdate()
    {
        Vector3 cenGlobal = go.transform.TransformPoint(cenLocal); // Center (global space)

        go.transform.RotateAround(cenGlobal, Vector3.up, deg);
    }
}
