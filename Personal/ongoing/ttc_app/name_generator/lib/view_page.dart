import 'package:flutter/material.dart';

class ViewPage extends StatefulWidget {
  static List<String> responses = []; // Static list to store responses

  @override
  _ViewPageState createState() => _ViewPageState();
}

class _ViewPageState extends State<ViewPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('View Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Responses:'),
            Expanded(
              child: ListView.builder(
                itemCount: ViewPage.responses.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(ViewPage.responses[index]),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
